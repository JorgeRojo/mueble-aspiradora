import os

html_content = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Render Fotorrealista Mueble Dreame - Cotas en Líneas Negras</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body, html { width: 100%; height: 100%; overflow: hidden; background: #e5e0d8; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }
    #canvas-container { width: 100%; height: 100%; position: absolute; top: 0; left: 0; }
    #svg-overlay { width: 100%; height: 100%; position: absolute; top: 0; left: 0; pointer-events: none; z-index: 10; }
  </style>
  <script src="three.min.js"></script>
</head>
<body>
  <div id="canvas-container"></div>
  <svg id="svg-overlay" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- Black architectural drafting arrow -->
      <marker id="arrow-black" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#111827" />
      </marker>
      <!-- Clean white halo filter for black text and lines (maximum contrast without ugly boxes) -->
      <filter id="halo" x="-30%" y="-30%" width="160%" height="160%">
        <feMorphology in="SourceAlpha" result="DILATED" operator="dilate" radius="2"/>
        <feFlood flood-color="#ffffff" flood-opacity="0.95" result="COLOR"/>
        <feComposite in="COLOR" in2="DILATED" operator="in" result="OUTLINE"/>
        <feMerge>
          <feMergeNode in="OUTLINE"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
  </svg>

  <script>
    // EXACT MILLIMETER SPECIFICATIONS (1 mm = 0.001 m)
    const W_EXT = 0.480;         // 480 mm overall width
    const H_EXT = 0.790;         // 790 mm overall height (compact)
    const D_EXT = 0.560;         // 560 mm overall depth
    const T_PLY = 0.023;         // 23 mm plywood thickness
    const H_NICHE = 0.040;       // 40 mm upper slot
    const H_BASE = 0.568;        // 568 mm Dreame base station height
    const W_BASE = 0.423;        // 423 mm Dreame base station width
    const D_BASE = 0.493;        // 493 mm Dreame base depth with ramp
    const W_VANO = 0.390;        // 390 mm robot floor opening
    const H_VANO = 0.117;        // 117 mm robot floor opening
    const W_STILE = 0.045;       // 45 mm side door stiles
    const W_HATCH = 0.410;       // 410 mm guillotine panel width
    const H_HATCH = 0.140;       // 140 mm guillotine panel height
    const W_RAIL = 0.020;        // 20 mm U-rail width
    const L_RAIL = 0.280;        // 280 mm U-rail length
    const STROKE_ACT = 0.150;    // 150 mm actuator stroke
    const L_ACT_RETRACT = 0.255; // 255 mm actuator retracted length

    const container = document.getElementById('canvas-container');
    const width = window.innerWidth;
    const height = window.innerHeight;

    const scene = new THREE.Scene();

    // Architectural eye-level 3/4 perspective framing the furniture
    const camera = new THREE.PerspectiveCamera(27, width / height, 0.1, 50);
    camera.position.set(1.72, 0.94, 1.84);
    camera.lookAt(-0.02, 0.37, 0.05);

    const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    // CRITICAL FOR PHOTOREALISM: Proper sRGB gamma pipeline
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.0;
    container.appendChild(renderer.domElement);

    // ================= HELPER FOR REALISTIC BEVELED PANELS =================
    function createBeveledBoxGeometry(w, h, d, r=0.002) {
      const shape = new THREE.Shape();
      shape.moveTo(-w/2 + r, -h/2);
      shape.lineTo(w/2 - r, -h/2);
      shape.quadraticCurveTo(w/2, -h/2, w/2, -h/2 + r);
      shape.lineTo(w/2, h/2 - r);
      shape.quadraticCurveTo(w/2, h/2, w/2 - r, h/2);
      shape.lineTo(-w/2 + r, h/2);
      shape.quadraticCurveTo(-w/2, h/2, -w/2, h/2 - r);
      shape.lineTo(-w/2, -h/2 + r);
      shape.quadraticCurveTo(-w/2, -h/2, -w/2 + r, -h/2);

      const geom = new THREE.ExtrudeGeometry(shape, {
        depth: d - 2 * r,
        bevelEnabled: true,
        bevelSegments: 3,
        steps: 1,
        bevelSize: r,
        bevelThickness: r
      });
      geom.center();
      return geom;
    }

    // ================= HIGH-END INDOOR ENVIRONMENT MAP (PBR REFLECTIONS) =================
    function createStudioEnvironmentMap() {
      const c = document.createElement('canvas');
      c.width = 1024;
      c.height = 512;
      const ctx = c.getContext('2d');

      // Base interior room gradient
      const bgGrad = ctx.createLinearGradient(0, 0, 0, c.height);
      bgGrad.addColorStop(0, '#faf7f2');   // Soft warm ceiling
      bgGrad.addColorStop(0.45, '#e8e2d8'); // Off-white walls
      bgGrad.addColorStop(1, '#8c5d33');   // Warm oak floor reflection bounce
      ctx.fillStyle = bgGrad;
      ctx.fillRect(0, 0, c.width, c.height);

      // Bright natural morning window on the right
      const winGrad = ctx.createRadialGradient(c.width * 0.75, c.height * 0.35, 15, c.width * 0.75, c.height * 0.35, 240);
      winGrad.addColorStop(0, '#ffffff');
      winGrad.addColorStop(0.25, '#fffaf2');
      winGrad.addColorStop(0.65, '#e2ebf7');
      winGrad.addColorStop(1, 'rgba(230, 225, 215, 0)');
      ctx.fillStyle = winGrad;
      ctx.fillRect(c.width * 0.5, 0, c.width * 0.5, c.height * 0.7);

      const tex = new THREE.CanvasTexture(c);
      tex.encoding = THREE.sRGBEncoding;
      tex.mapping = THREE.EquirectangularReflectionMapping;

      const pmrem = new THREE.PMREMGenerator(renderer);
      pmrem.compileEquirectangularShader();
      const envMap = pmrem.fromEquirectangular(tex).texture;
      pmrem.dispose();
      return envMap;
    }

    const envMap = createStudioEnvironmentMap();
    scene.environment = envMap;

    // ================= PHOTOREALISTIC NATURAL OAK HERRINGBONE PARQUET =================
    function createOakParquetTexture() {
      const c = document.createElement('canvas');
      c.width = 2048;
      c.height = 2048;
      const ctx = c.getContext('2d');

      // Authentic warm Scandinavian natural oak base
      ctx.fillStyle = '#b88959';
      ctx.fillRect(0, 0, c.width, c.height);

      const pW = 56;
      const pH = 224;
      // High-contrast, rich authentic oak plank palette
      const tones = [
        '#c49563', '#bb8652', '#d09f6b', '#b37f48',
        '#c99867', '#ab7640', '#d6a673', '#b8854f',
        '#c18f5a', '#a6723c', '#cc9c6a', '#b7834c'
      ];

      for (let y = -pH; y < c.height + pH; y += pW * 2) {
        for (let x = -pH; x < c.width + pH; x += pH) {
          ctx.save();
          ctx.translate(x, y);
          for (let i = 0; i < 2; i++) {
            // Plank wood base
            const plankColor = tones[Math.floor(Math.random() * tones.length)];
            ctx.fillStyle = plankColor;
            ctx.fillRect(0, 0, pW, pH);

            // Fine wood grain fibers & growth rings
            ctx.strokeStyle = 'rgba(50, 25, 6, 0.14)';
            ctx.lineWidth = 1.0;
            for (let g = 3; g < pW; g += 5) {
              ctx.beginPath();
              ctx.moveTo(g, 0);
              const curl = (Math.random() - 0.5) * 5;
              ctx.bezierCurveTo(g + curl, pH * 0.35, g - curl, pH * 0.7, g, pH);
              ctx.stroke();
            }

            // Dark bevel seam (chanfrein)
            ctx.strokeStyle = '#221105';
            ctx.lineWidth = 1.6;
            ctx.strokeRect(0, 0, pW, pH);

            // Subtle specular edge highlight
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.22)';
            ctx.lineWidth = 0.8;
            ctx.beginPath();
            ctx.moveTo(1, 1); ctx.lineTo(1, pH - 1);
            ctx.moveTo(1, 1); ctx.lineTo(pW - 1, 1);
            ctx.stroke();

            ctx.translate(pW, 0);
            ctx.rotate(Math.PI / 2);
          }
          ctx.restore();
        }
      }

      const tex = new THREE.CanvasTexture(c);
      tex.encoding = THREE.sRGBEncoding;
      tex.wrapS = THREE.RepeatWrapping;
      tex.wrapT = THREE.RepeatWrapping;
      tex.repeat.set(5.5, 5.5);
      return tex;
    }

    const floorTex = createOakParquetTexture();
    const floorMat = new THREE.MeshStandardMaterial({
      map: floorTex,
      roughness: 0.24,
      metalness: 0.03
    });

    const floor = new THREE.Mesh(new THREE.PlaneGeometry(16, 16), floorMat);
    floor.rotation.x = -Math.PI / 2;
    floor.receiveShadow = true;
    scene.add(floor);

    // Scandinavian Off-white Plaster Wall
    const wallMat = new THREE.MeshStandardMaterial({
      color: 0xf6f4ee,
      roughness: 0.88,
      metalness: 0.0
    });

    const backWall = new THREE.Mesh(new THREE.PlaneGeometry(16, 6), wallMat);
    backWall.position.set(0, 3, -D_EXT * 0.65);
    backWall.receiveShadow = true;
    scene.add(backWall);

    const leftWall = new THREE.Mesh(new THREE.PlaneGeometry(16, 6), wallMat);
    leftWall.rotation.y = Math.PI / 2;
    leftWall.position.set(-2.5, 3, 0);
    leftWall.receiveShadow = true;
    scene.add(leftWall);

    // White Skirting Board (Rodapié)
    const skirtingMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.22 });
    const skirtBack = new THREE.Mesh(new THREE.BoxGeometry(16, 0.08, 0.015), skirtingMat);
    skirtBack.position.set(0, 0.04, -D_EXT * 0.65 + 0.0075);
    scene.add(skirtBack);

    // ================= LIGHTING & PHYSICAL CONTACT SHADOWS =================
    // Morning natural sunlight from window (casts soft diagonal shadows across floor to the left)
    const sun = new THREE.DirectionalLight(0xfff6ea, 1.8);
    sun.position.set(3.2, 3.8, 1.2);
    sun.castShadow = true;
    sun.shadow.mapSize.width = 4096;
    sun.shadow.mapSize.height = 4096;
    sun.shadow.camera.near = 0.5;
    sun.shadow.camera.far = 14;
    sun.shadow.camera.left = -1.8;
    sun.shadow.camera.right = 1.8;
    sun.shadow.camera.top = 2.4;
    sun.shadow.camera.bottom = -1.2;
    sun.shadow.bias = -0.00008;
    sun.shadow.radius = 2.8;
    scene.add(sun);

    // Parquet bounce light
    const hemi = new THREE.HemisphereLight(0xffffff, 0xb88959, 0.5);
    scene.add(hemi);

    // Soft warm interior fill light
    const interiorFill = new THREE.PointLight(0xfffaee, 0.35, 8);
    interiorFill.position.set(0.1, 0.8, 1.4);
    scene.add(interiorFill);

    // Contact ambient occlusion shadow under cabinet edges & base
    function createContactShadowTexture() {
      const c = document.createElement('canvas');
      c.width = 512;
      c.height = 512;
      const ctx = c.getContext('2d');
      const grad = ctx.createRadialGradient(256, 256, 20, 256, 256, 230);
      grad.addColorStop(0, 'rgba(20, 10, 2, 0.65)');
      grad.addColorStop(0.35, 'rgba(20, 10, 2, 0.28)');
      grad.addColorStop(1, 'rgba(20, 10, 2, 0.0)');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, 512, 512);
      return new THREE.CanvasTexture(c);
    }
    const contactShadowMat = new THREE.MeshBasicMaterial({
      map: createContactShadowTexture(),
      transparent: true,
      depthWrite: false
    });
    const contactShadow = new THREE.Mesh(new THREE.PlaneGeometry(1.3, 1.3), contactShadowMat);
    contactShadow.rotation.x = -Math.PI / 2;
    contactShadow.position.set(-0.02, 0.001, 0.08);
    scene.add(contactShadow);

    // ================= PBR MATERIALS =================
    // Matte warm white lacquer (100% white painted edges, seamless finish)
    const whiteLacquerMat = new THREE.MeshStandardMaterial({
      color: 0xfbfaf8,
      roughness: 0.28,
      metalness: 0.01
    });

    // Satin Anodized Aluminum (rails & actuator housing)
    const aluMat = new THREE.MeshStandardMaterial({
      color: 0xdde2ea,
      roughness: 0.20,
      metalness: 0.88
    });

    // Mirror Polished Chrome (actuator piston rod)
    const chromeMat = new THREE.MeshStandardMaterial({
      color: 0xffffff,
      roughness: 0.02,
      metalness: 0.98
    });

    // Dreame robot & dock materials
    const dreameGlossWhite = new THREE.MeshStandardMaterial({
      color: 0xffffff,
      roughness: 0.12,
      metalness: 0.02
    });
    const dreameGold = new THREE.MeshStandardMaterial({
      color: 0xc8b08c,
      roughness: 0.22,
      metalness: 0.82
    });
    const darkAcrylic = new THREE.MeshStandardMaterial({
      color: 0x181a1f,
      roughness: 0.08,
      metalness: 0.88
    });

    // Space Gray Aluminum laptop
    const laptopMat = new THREE.MeshStandardMaterial({
      color: 0x5a5d64,
      roughness: 0.20,
      metalness: 0.85
    });

    // ================= CABINET 3D ASSEMBLY (EXACT TO CUTTING LIST) =================
    const cabinet = new THREE.Group();
    scene.add(cabinet);

    const zBack = -D_EXT / 2;
    const zFront = D_EXT / 2 - T_PLY; // front face before door
    const hSide = H_EXT - T_PLY;      // 0.767 m
    const dSide = D_EXT - T_PLY;      // 0.537 m
    const wInt = W_EXT - 2 * T_PLY;   // 0.434 m

    // 1. Left Side Panel (0.023 x 0.767 x 0.537) - Rests on floor
    const leftSideGeom = createBeveledBoxGeometry(T_PLY, hSide, dSide);
    const leftSide = new THREE.Mesh(leftSideGeom, whiteLacquerMat);
    leftSide.position.set(-W_EXT / 2 + T_PLY / 2, hSide / 2, (zBack + zFront) / 2);
    leftSide.castShadow = true;
    leftSide.receiveShadow = true;
    cabinet.add(leftSide);

    // 2. Right Side Panel (0.023 x 0.767 x 0.537) - Rests on floor
    const rightSideGeom = createBeveledBoxGeometry(T_PLY, hSide, dSide);
    const rightSide = new THREE.Mesh(rightSideGeom, whiteLacquerMat);
    rightSide.position.set(W_EXT / 2 - T_PLY / 2, hSide / 2, (zBack + zFront) / 2);
    rightSide.castShadow = true;
    rightSide.receiveShadow = true;
    cabinet.add(rightSide);

    // 3. Top Counter (0.480 x 0.023 x 0.537) - Sits ON TOP of side panels!
    const topCounterGeom = createBeveledBoxGeometry(W_EXT, T_PLY, dSide);
    const topCounter = new THREE.Mesh(topCounterGeom, whiteLacquerMat);
    topCounter.position.set(0, H_EXT - T_PLY / 2, (zBack + zFront) / 2);
    topCounter.castShadow = true;
    topCounter.receiveShadow = true;
    cabinet.add(topCounter);

    // 4. Internal Shelf (0.434 x 0.023 x 0.530) - EXACTLY 40 mm slot beneath top panel!
    const dShelf = dSide - 0.007; // 0.530 m
    const shelfGeom = createBeveledBoxGeometry(wInt, T_PLY, dShelf);
    const shelfMesh = new THREE.Mesh(shelfGeom, whiteLacquerMat);
    shelfMesh.position.set(0, 0.7155, (zBack + zFront) / 2);
    shelfMesh.castShadow = true;
    shelfMesh.receiveShadow = true;
    cabinet.add(shelfMesh);

    // 5. Aluminum Laptop on top exterior counter
    const laptopGroup = new THREE.Group();
    laptopGroup.position.set(0.01, H_EXT, 0.02);
    laptopGroup.rotation.y = 0.04;
    cabinet.add(laptopGroup);

    const laptopBase = new THREE.Mesh(new THREE.BoxGeometry(0.31, 0.008, 0.22), laptopMat);
    laptopBase.position.y = 0.004;
    laptopBase.castShadow = true;
    laptopGroup.add(laptopBase);

    const laptopLid = new THREE.Mesh(new THREE.BoxGeometry(0.31, 0.004, 0.22), laptopMat);
    laptopLid.position.y = 0.010;
    laptopLid.castShadow = true;
    laptopGroup.add(laptopLid);

    // ================= DREAME BASE STATION (ON FLOOR AT COTA CERO) =================
    const baseGroup = new THREE.Group();
    baseGroup.position.set(0, 0, 0.02);
    cabinet.add(baseGroup);

    // Base Station Body: 0.423 W x 0.568 H x 0.340 D with filleted front edges
    const baseShape = new THREE.Shape();
    const bW = W_BASE;
    const bD = 0.34;
    const bR = 0.025; // corner radius
    baseShape.moveTo(-bW/2 + bR, -bD/2);
    baseShape.lineTo(bW/2 - bR, -bD/2);
    baseShape.quadraticCurveTo(bW/2, -bD/2, bW/2, -bD/2 + bR);
    baseShape.lineTo(bW/2, bD/2 - bR);
    baseShape.quadraticCurveTo(bW/2, bD/2, bW/2 - bR, bD/2);
    baseShape.lineTo(-bW/2 + bR, bD/2);
    baseShape.quadraticCurveTo(-bW/2, bD/2, -bW/2, bD/2 - bR);
    baseShape.lineTo(-bW/2, -bD/2 + bR);
    baseShape.quadraticCurveTo(-bW/2, -bD/2, -bW/2 + bR, -bD/2);

    const baseGeom = new THREE.ExtrudeGeometry(baseShape, {
      depth: H_BASE,
      bevelEnabled: true,
      bevelSegments: 4,
      steps: 1,
      bevelSize: 0.003,
      bevelThickness: 0.003
    });
    baseGeom.center();
    const baseBody = new THREE.Mesh(baseGeom, dreameGlossWhite);
    baseBody.rotation.x = -Math.PI / 2;
    baseBody.position.set(0, H_BASE / 2, -0.06);
    baseBody.castShadow = true;
    baseBody.receiveShadow = true;
    baseGroup.add(baseBody);

    // Twin water tank lid tops (clean water / waste water)
    const tankLidL = new THREE.Mesh(new THREE.BoxGeometry(0.19, 0.006, 0.31), darkAcrylic);
    tankLidL.position.set(-0.102, H_BASE + 0.003, -0.06);
    baseGroup.add(tankLidL);

    const tankLidR = new THREE.Mesh(new THREE.BoxGeometry(0.19, 0.006, 0.31), darkAcrylic);
    tankLidR.position.set(0.102, H_BASE + 0.003, -0.06);
    baseGroup.add(tankLidR);

    // Champagne gold decorative metallic band across middle
    const goldStrip = new THREE.Mesh(new THREE.BoxGeometry(W_BASE + 0.002, 0.060, 0.344), dreameGold);
    goldStrip.position.set(0, 0.22, -0.06);
    baseGroup.add(goldStrip);

    // Status LED display oval in the gold band
    const ledDisplay = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.020, 0.002), darkAcrylic);
    ledDisplay.position.set(0, 0.22, 0.113);
    baseGroup.add(ledDisplay);

    // Lower dock wash cavity
    const dockBay = new THREE.Mesh(new THREE.BoxGeometry(0.38, 0.12, 0.18), darkAcrylic);
    dockBay.position.set(0, 0.06, 0.05);
    baseGroup.add(dockBay);

    // Dock floor ramp
    const ramp = new THREE.Mesh(new THREE.BoxGeometry(0.38, 0.012, 0.22), dreameGlossWhite);
    ramp.position.set(0, 0.006, 0.17);
    ramp.receiveShadow = true;
    baseGroup.add(ramp);

    // Circular Dreame Robot (Ø350 mm x 97 mm height)
    const robot = new THREE.Group();
    robot.position.set(0, 0, 0.18);
    baseGroup.add(robot);

    const robotBody = new THREE.Mesh(new THREE.CylinderGeometry(0.175, 0.175, 0.080, 64), dreameGlossWhite);
    robotBody.position.y = 0.040;
    robotBody.castShadow = true;
    robot.add(robotBody);

    // Front obstacle avoidance camera window
    const frontSensor = new THREE.Mesh(new THREE.BoxGeometry(0.09, 0.025, 0.01), darkAcrylic);
    frontSensor.position.set(0, 0.045, 0.175);
    robot.add(frontSensor);

    // LDS laser tower
    const lidarTurret = new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.045, 0.017, 36), darkAcrylic);
    lidarTurret.position.set(0, 0.088, -0.02);
    robot.add(lidarTurret);

    const lidarCap = new THREE.Mesh(new THREE.CylinderGeometry(0.042, 0.042, 0.004, 36), dreameGold);
    lidarCap.position.set(0, 0.098, -0.02);
    robot.add(lidarCap);

    // ================= FULL OVERLAY DOOR WITH GUILLOTINE & ACTUATOR =================
    // Hinged at front-left edge of cabinet: x = -W_EXT / 2, z = D_EXT / 2
    const doorHinge = new THREE.Group();
    doorHinge.position.set(-W_EXT / 2, 0, D_EXT / 2);
    doorHinge.rotation.y = -Math.PI * 0.44; // Swung open ~80 degrees
    cabinet.add(doorHinge);

    // Left Stile (45 mm W x 117 mm H x 23 mm T)
    const leftStileGeom = createBeveledBoxGeometry(W_STILE, H_VANO, T_PLY);
    const leftStile = new THREE.Mesh(leftStileGeom, whiteLacquerMat);
    leftStile.position.set(W_STILE / 2, H_VANO / 2, -T_PLY / 2);
    leftStile.castShadow = true;
    doorHinge.add(leftStile);

    // Right Stile (45 mm W x 117 mm H x 23 mm T)
    const rightStileGeom = createBeveledBoxGeometry(W_STILE, H_VANO, T_PLY);
    const rightStile = new THREE.Mesh(rightStileGeom, whiteLacquerMat);
    rightStile.position.set(W_EXT - W_STILE / 2, H_VANO / 2, -T_PLY / 2);
    rightStile.castShadow = true;
    doorHinge.add(rightStile);

    // Main Upper Door (480 mm W x (790 - 117 = 673 mm) H x 23 mm T)
    const hUpper = H_EXT - H_VANO;
    const upperDoorGeom = createBeveledBoxGeometry(W_EXT, hUpper, T_PLY);
    const upperDoor = new THREE.Mesh(upperDoorGeom, whiteLacquerMat);
    upperDoor.position.set(W_EXT / 2, H_VANO + hUpper / 2, -T_PLY / 2);
    upperDoor.castShadow = true;
    doorHinge.add(upperDoor);

    // Two Extruded Aluminum U-channel guide rails
    function createURailGeometry(length) {
      const shape = new THREE.Shape();
      const w = 0.020;  // 20 mm width
      const d = 0.015;  // 15 mm depth
      const t = 0.002;  // 2 mm wall
      shape.moveTo(0, 0);
      shape.lineTo(w, 0);
      shape.lineTo(w, d);
      shape.lineTo(w - t, d);
      shape.lineTo(w - t, t);
      shape.lineTo(t, t);
      shape.lineTo(t, d);
      shape.lineTo(0, d);
      shape.closePath();

      return new THREE.ExtrudeGeometry(shape, {
        depth: length,
        bevelEnabled: false
      });
    }

    const railGeom = createURailGeometry(L_RAIL);

    const leftRail = new THREE.Mesh(railGeom, aluMat);
    leftRail.rotation.x = -Math.PI / 2;
    leftRail.position.set(0.025, 0, -T_PLY - 0.015);
    leftRail.castShadow = true;
    doorHinge.add(leftRail);

    const rightRail = new THREE.Mesh(railGeom, aluMat);
    rightRail.rotation.x = -Math.PI / 2;
    rightRail.position.set(W_EXT - 0.045, 0, -T_PLY - 0.015);
    rightRail.castShadow = true;
    doorHinge.add(rightRail);

    // Sliding Guillotine Hatch Panel (410 mm W x 140 mm H x 12 mm T)
    // IN RAISED POSITION: Lifted 125 mm up (leaves 117 mm floor vano 100% clear at Cota Cero)
    const hatchLift = 0.125;
    const hatchGeom = createBeveledBoxGeometry(W_HATCH, H_HATCH, 0.012, 0.0015);
    const hatchMesh = new THREE.Mesh(hatchGeom, whiteLacquerMat);
    hatchMesh.position.set(W_EXT / 2, hatchLift + H_HATCH / 2, -T_PLY - 0.006);
    hatchMesh.castShadow = true;
    doorHinge.add(hatchMesh);

    // Bracket on panel top
    const panelBracket = new THREE.Mesh(new THREE.BoxGeometry(0.032, 0.016, 0.020), aluMat);
    panelBracket.position.set(W_EXT / 2, hatchLift + H_HATCH + 0.008, -T_PLY - 0.012);
    doorHinge.add(panelBracket);

    // 12V Micro Linear Actuator (Carrera 150 mm, Longitud retraído 255 mm)
    // Actuator cylinder body (Brushed Aluminum)
    const actBody = new THREE.Mesh(new THREE.CylinderGeometry(0.013, 0.013, 0.165, 24), aluMat);
    actBody.position.set(W_EXT / 2, hatchLift + H_HATCH + 0.142, -T_PLY - 0.018);
    actBody.castShadow = true;
    doorHinge.add(actBody);

    // Top Motor Housing & Door Mount Clevis
    const actMotor = new THREE.Mesh(new THREE.BoxGeometry(0.042, 0.052, 0.032), aluMat);
    actMotor.position.set(W_EXT / 2, hatchLift + H_HATCH + 0.228, -T_PLY - 0.020);
    actMotor.castShadow = true;
    doorHinge.add(actMotor);

    // Polished Chrome Extension Rod (150 mm Stroke)
    const actRod = new THREE.Mesh(new THREE.CylinderGeometry(0.006, 0.006, 0.145, 24), chromeMat);
    actRod.position.set(W_EXT / 2, hatchLift + H_HATCH + 0.052, -T_PLY - 0.018);
    doorHinge.add(actRod);

    // Concealed European Cup Hinges (Bisagras de cazoleta)
    const hTop = new THREE.Mesh(new THREE.BoxGeometry(0.022, 0.065, 0.035), aluMat);
    hTop.position.set(0.015, H_EXT - 0.12, -0.01);
    doorHinge.add(hTop);

    const hBot = new THREE.Mesh(new THREE.BoxGeometry(0.022, 0.065, 0.035), aluMat);
    hBot.position.set(0.015, 0.22, -0.01);
    doorHinge.add(hBot);

    renderer.render(scene, camera);

    // ================= ARCHITECTURAL BLACK DIMENSION LINES (NO BADGES, NO TEXTS) =================
    const svg = document.getElementById('svg-overlay');

    function toScreen(vec3) {
      const v = vec3.clone();
      v.project(camera);
      return {
        x: (v.x * 0.5 + 0.5) * width,
        y: (-v.y * 0.5 + 0.5) * height
      };
    }

    // Draw architectural black dimension line between two 3D world points
    function drawBlackDim(p1, p2, text, offsetScreen, flipText=false, horizontalText=false, customTextPos=null) {
      const s1 = toScreen(p1);
      const s2 = toScreen(p2);
      const dx = s2.x - s1.x;
      const dy = s2.y - s1.y;
      const len = Math.hypot(dx, dy);
      if (len === 0) return;
      const nx = -dy / len;
      const ny = dx / len;

      const o1 = { x: s1.x + nx * offsetScreen, y: s1.y + ny * offsetScreen };
      const o2 = { x: s2.x + nx * offsetScreen, y: s2.y + ny * offsetScreen };

      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");

      // 1. Witness / Extension lines (thin black lines with halo)
      const ext1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
      ext1.setAttribute("x1", s1.x); ext1.setAttribute("y1", s1.y);
      ext1.setAttribute("x2", s1.x + nx * (offsetScreen + (offsetScreen > 0 ? 5 : -5))); 
      ext1.setAttribute("y2", s1.y + ny * (offsetScreen + (offsetScreen > 0 ? 5 : -5)));
      ext1.setAttribute("stroke", "#111827"); ext1.setAttribute("stroke-width", "1.2");
      ext1.setAttribute("filter", "url(#halo)");
      g.appendChild(ext1);

      const ext2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
      ext2.setAttribute("x1", s2.x); ext2.setAttribute("y1", s2.y);
      ext2.setAttribute("x2", s2.x + nx * (offsetScreen + (offsetScreen > 0 ? 5 : -5))); 
      ext2.setAttribute("y2", s2.y + ny * (offsetScreen + (offsetScreen > 0 ? 5 : -5)));
      ext2.setAttribute("stroke", "#111827"); ext2.setAttribute("stroke-width", "1.2");
      ext2.setAttribute("filter", "url(#halo)");
      g.appendChild(ext2);

      // 2. Main dimension line with arrowheads
      const dimLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
      dimLine.setAttribute("x1", o1.x); dimLine.setAttribute("y1", o1.y);
      dimLine.setAttribute("x2", o2.x); dimLine.setAttribute("y2", o2.y);
      dimLine.setAttribute("stroke", "#111827"); dimLine.setAttribute("stroke-width", "1.5");
      dimLine.setAttribute("marker-start", "url(#arrow-black)");
      dimLine.setAttribute("marker-end", "url(#arrow-black)");
      dimLine.setAttribute("filter", "url(#halo)");
      g.appendChild(dimLine);

      // 3. Crisp black dimension number centered on line (pure number + unit, NO WORDS)
      let mx = (o1.x + o2.x) / 2;
      let my = (o1.y + o2.y) / 2;
      if (customTextPos) {
        mx = customTextPos.x;
        my = customTextPos.y;
      }

      let rot = 0;
      if (!horizontalText) {
        const angle = Math.atan2(dy, dx) * 180 / Math.PI;
        rot = (angle > 90 || angle < -90) ? angle + 180 : angle;
      }

      const textEl = document.createElementNS("http://www.w3.org/2000/svg", "text");
      textEl.textContent = text;
      textEl.setAttribute("font-size", "14");
      textEl.setAttribute("font-weight", "800");
      textEl.setAttribute("fill", "#111827");
      textEl.setAttribute("text-anchor", "middle");
      textEl.setAttribute("filter", "url(#halo)");
      
      const tDist = flipText ? 12 : -8;
      textEl.setAttribute("transform", `translate(${mx + nx * tDist}, ${my + ny * tDist}) rotate(${rot})`);
      g.appendChild(textEl);

      svg.appendChild(g);
    }

    // World Coordinates for dimensions
    const pTopFrontLeft = new THREE.Vector3(-W_EXT / 2, H_EXT, zFront);
    const pTopFrontRight = new THREE.Vector3(W_EXT / 2, H_EXT, zFront);
    const pTopBackRight = new THREE.Vector3(W_EXT / 2, H_EXT, zBack);
    const pBotRight = new THREE.Vector3(W_EXT / 2, 0, zFront);

    // 1. ANCHO EXTERIOR: 480 mm (En encimera superior)
    drawBlackDim(pTopFrontLeft, pTopFrontRight, "480 mm", -35);

    // 2. ALTO TOTAL: 790 mm (Exterior derecho limpio)
    drawBlackDim(pTopFrontRight, pBotRight, "790 mm", -55, false, true);

    // 3. FONDO EXTERIOR: 560 mm (Lateral superior)
    drawBlackDim(pTopFrontRight, pTopBackRight, "560 mm", -35);

    // 4. ESPESOR TABLERO: 23 mm (Canto frontal izquierdo)
    const pEdge1 = new THREE.Vector3(-W_EXT / 2, H_EXT - T_PLY / 2, zFront);
    const pEdge2 = new THREE.Vector3(-W_EXT / 2 + T_PLY, H_EXT - T_PLY / 2, zFront);
    drawBlackDim(pEdge1, pEdge2, "23 mm", -25);

    // 5. RANURA SUPERIOR: 40 mm (Entre encimera y balda interior)
    const pNicheTop = new THREE.Vector3(0.04, H_EXT - T_PLY, zFront);
    const pNicheBot = new THREE.Vector3(0.04, H_EXT - T_PLY - H_NICHE, zFront);
    drawBlackDim(pNicheTop, pNicheBot, "40 mm", -25, false, true);

    // 6. ESPACIO DEPÓSITOS: 136 mm (Entre base y balda interior)
    const pTankTop = new THREE.Vector3(0.12, 0.704, 0.0);
    const pTankBot = new THREE.Vector3(0.12, 0.568, 0.0);
    drawBlackDim(pTankTop, pTankBot, "136 mm", 28, false, true);

    // 7. ALTURA BASE DREAME: 568 mm (Vertical directamente en el frontal de la base)
    const pBaseTop = new THREE.Vector3(W_BASE / 2 - 0.02, H_BASE, 0.11);
    const pBaseBot = new THREE.Vector3(W_BASE / 2 - 0.02, 0, 0.11);
    drawBlackDim(pBaseTop, pBaseBot, "568 mm", 24, false, true);

    // DIMENSIONES EN LA PUERTA (Coordenadas locales transformadas a mundo)
    doorHinge.updateMatrixWorld(true);

    // 8. ANCHO VANO ROBOT COTA CERO: 390 mm (A ras de suelo, offset hacia abajo)
    const pVanoLeft = new THREE.Vector3(0.045, 0.005, 0).applyMatrix4(doorHinge.matrixWorld);
    const pVanoRight = new THREE.Vector3(0.435, 0.005, 0).applyMatrix4(doorHinge.matrixWorld);
    drawBlackDim(pVanoLeft, pVanoRight, "390 mm", -34);

    // 9. ALTO VANO ROBOT COTA CERO: 117 mm (Vertical en el borde interior del montante izquierdo)
    const pVanoLBot = new THREE.Vector3(W_EXT - 0.045, 0.0, 0).applyMatrix4(doorHinge.matrixWorld);
    const pVanoLTop = new THREE.Vector3(W_EXT - 0.045, 0.117, 0).applyMatrix4(doorHinge.matrixWorld);
    drawBlackDim(pVanoLBot, pVanoLTop, "117 mm", 20, false, true);

    // 10. ANCHO MONTANTE PUERTA: 45 mm (Montante exterior en la parte inferior)
    const pStile1 = new THREE.Vector3(W_EXT - 0.045, 0.035, 0).applyMatrix4(doorHinge.matrixWorld);
    const pStile2 = new THREE.Vector3(W_EXT, 0.035, 0).applyMatrix4(doorHinge.matrixWorld);
    drawBlackDim(pStile1, pStile2, "45 mm", -22);

    // 11. ANCHO COMPUERTA GUILLOTINA: 410 mm (En la parte media-alta de la compuerta, limpia)
    const pHatchLeft = new THREE.Vector3(0.035, hatchLift + 0.07, -0.012).applyMatrix4(doorHinge.matrixWorld);
    const pHatchRight = new THREE.Vector3(0.445, hatchLift + 0.07, -0.012).applyMatrix4(doorHinge.matrixWorld);
    drawBlackDim(pHatchLeft, pHatchRight, "410 mm", -18);

    // 12. ALTO COMPUERTA GUILLOTINA: 140 mm (Vertical en lateral izquierdo de la compuerta)
    const pHatchLBot = new THREE.Vector3(0.035, hatchLift, -0.012).applyMatrix4(doorHinge.matrixWorld);
    const pHatchLTop = new THREE.Vector3(0.035, hatchLift + H_HATCH, -0.012).applyMatrix4(doorHinge.matrixWorld);
    drawBlackDim(pHatchLBot, pHatchLTop, "140 mm", -25, false, true);

    // 13. CARRERA ACTUADOR LINEAL: 150 mm (Vertical en vástago de actuador, offset hacia la izquierda)
    const pActRodBot = new THREE.Vector3(W_EXT / 2, hatchLift + H_HATCH, -0.018).applyMatrix4(doorHinge.matrixWorld);
    const pActRodTop = new THREE.Vector3(W_EXT / 2, hatchLift + H_HATCH + 0.150, -0.018).applyMatrix4(doorHinge.matrixWorld);
    drawBlackDim(pActRodBot, pActRodTop, "150 mm", -30, false, true);

    // 14. ANCHO RIEL GUÍA EN U: 20 mm (Extremo superior del riel derecho)
    const pRail1 = new THREE.Vector3(0.025, 0.280, -0.015).applyMatrix4(doorHinge.matrixWorld);
    const pRail2 = new THREE.Vector3(0.045, 0.280, -0.015).applyMatrix4(doorHinge.matrixWorld);
    drawBlackDim(pRail1, pRail2, "20 mm", -22);

    // Render final frame
    renderer.render(scene, camera);
    window.__RENDER_READY__ = true;
  </script>
</body>
</html>
'''

with open('/Users/jorge/projects/mueble-aspiradora/render_3d_photorealistic.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Saved updated render_3d_photorealistic.html v4")
