import math
import subprocess
import os
from PIL import Image

def generate_blueprint():
    width = 2560
    height = 1600
    
    # SVG string
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #0d1527; font-family: -apple-system, BlinkMacSystemFont, \'SF Pro Display\', \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')
    
    # Grid pattern & definitions
    svg.append('''
    <defs>
      <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
        <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#182642" stroke-width="1"/>
      </pattern>
      <pattern id="grid-major" width="200" height="200" patternUnits="userSpaceOnUse">
        <rect width="200" height="200" fill="url(#grid)" />
        <path d="M 200 0 L 0 0 0 200" fill="none" stroke="#22365d" stroke-width="1.5"/>
      </pattern>
      <marker id="arrow-cyan" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#00f2fe" />
      </marker>
      <marker id="arrow-orange" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#ff9e00" />
      </marker>
      <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="3" result="blur" />
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    <rect width="100%" height="100%" fill="url(#grid-major)" />
    ''')
    
    # Title & Metadata Block
    svg.append('''
    <g id="title-block" transform="translate(100, 80)">
      <rect x="0" y="0" width="750" height="120" rx="8" fill="#131e36" stroke="#2a4374" stroke-width="2" />
      <text x="30" y="45" font-size="28" font-weight="900" fill="#ffffff" letter-spacing="1.5">PLANOS TÉCNICOS 3D WIREFRAME</text>
      <text x="30" y="75" font-size="16" font-weight="700" fill="#00f2fe" letter-spacing="1">MUEBLE COTA CERO · ROBOT DREAME · SOLAPE TOTAL</text>
      <text x="30" y="100" font-size="13" font-weight="500" fill="#8da2c0">ANCHO MÍNIMO: 480 mm | ALTO: 790 mm | FONDO: 560 mm | CONTRACHAPADO: 23 mm</text>
    </g>
    ''')
    
    # 3D Isometric Projection Helper
    # Model space (mm):
    # X: Width (0 to 480), goes to the right-down
    # Y: Height (0 to 790), goes straight UP
    # Z: Depth (0 to 560), goes to the left-down (towards user)
    iso_ox = 1150
    iso_oy = 1180
    iso_scale = 1.15
    angle = math.radians(28)
    
    def project(x, y, z):
        # Isometric projection
        # x goes right (+cos, +sin)
        # z goes left (-cos, +sin)
        # y goes up (-y)
        sx = iso_ox + (x * math.cos(angle) - z * math.cos(angle)) * iso_scale
        sy = iso_oy - y * iso_scale + (x * math.sin(angle) + z * math.sin(angle)) * iso_scale
        return sx, sy

    def draw_box(x0, y0, z0, dx, dy, dz, stroke="#4cc9f0", fill="rgba(76, 201, 240, 0.04)", stroke_width=2, stroke_dash="none"):
        # 8 corners
        c = [
            project(x0, y0, z0),          # 0: back-left-bot
            project(x0 + dx, y0, z0),     # 1: back-right-bot
            project(x0 + dx, y0 + dy, z0),# 2: back-right-top
            project(x0, y0 + dy, z0),     # 3: back-left-top
            project(x0, y0, z0 + dz),     # 4: front-left-bot
            project(x0 + dx, y0, z0 + dz),# 5: front-right-bot
            project(x0 + dx, y0 + dy, z0 + dz), # 6: front-right-top
            project(x0, y0 + dy, z0 + dz) # 7: front-left-top
        ]
        
        # Faces
        faces = [
            [0, 1, 2, 3], # back
            [4, 5, 6, 7], # front
            [0, 4, 7, 3], # left
            [1, 5, 6, 2], # right
            [3, 2, 6, 7], # top
            [0, 1, 5, 4]  # bot
        ]
        res = []
        for face in faces:
            pts = " ".join([f"{c[i][0]:.1f},{c[i][1]:.1f}" for i in face])
            res.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-dasharray="{stroke_dash}" stroke-linejoin="round" />')
        return "\n".join(res)

    def draw_line_3d(p1, p2, stroke="#00f2fe", stroke_width=2, stroke_dash="none", marker_end="", marker_start=""):
        s1 = project(*p1)
        s2 = project(*p2)
        m_end = f'marker-end="url(#{marker_end})"' if marker_end else ''
        m_start = f'marker-start="url(#{marker_start})"' if marker_start else ''
        return f'<line x1="{s1[0]:.1f}" y1="{s1[1]:.1f}" x2="{s2[0]:.1f}" y2="{s2[1]:.1f}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-dasharray="{stroke_dash}" {m_start} {m_end} />'

    def draw_dim_3d(p1, p2, text, offset_vec=(0,0,0), stroke="#00f2fe", text_color="#00f2fe", text_offset=(0,-10), font_size=15):
        # Draw dimension line with arrows and label
        op1 = (p1[0] + offset_vec[0], p1[1] + offset_vec[1], p1[2] + offset_vec[2])
        op2 = (p2[0] + offset_vec[0], p2[1] + offset_vec[1], p2[2] + offset_vec[2])
        lines = []
        # witness lines
        lines.append(draw_line_3d(p1, op1, stroke="#2a4374", stroke_width=1.5, stroke_dash="4,3"))
        lines.append(draw_line_3d(p2, op2, stroke="#2a4374", stroke_width=1.5, stroke_dash="4,3"))
        # dim line
        lines.append(draw_line_3d(op1, op2, stroke=stroke, stroke_width=2, marker_start="arrow-cyan" if stroke=="#00f2fe" else "arrow-orange", marker_end="arrow-cyan" if stroke=="#00f2fe" else "arrow-orange"))
        # text
        sp1 = project(*op1)
        sp2 = project(*op2)
        mx = (sp1[0] + sp2[0]) / 2 + text_offset[0]
        my = (sp1[1] + sp2[1]) / 2 + text_offset[1]
        lines.append(f'<rect x="{mx-len(text)*4.5-8:.1f}" y="{my-14:.1f}" width="{len(text)*9+16}" height="24" rx="4" fill="#0d1527" stroke="{stroke}" stroke-width="1.2" />')
        lines.append(f'<text x="{mx:.1f}" y="{my+3:.1f}" font-size="{font_size}" font-weight="700" fill="{text_color}" text-anchor="middle">{text}</text>')
        return "\n".join(lines)

    # 1. FLOOR LEVEL GRID (COTA CERO)
    svg.append('<g id="floor-grid">')
    for x in range(-100, 601, 100):
        p1 = project(x, 0, -50)
        p2 = project(x, 0, 650)
        svg.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="#16274a" stroke-width="1.5" />')
    for z in range(-50, 651, 100):
        p1 = project(-100, 0, z)
        p2 = project(600, 0, z)
        svg.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="#16274a" stroke-width="1.5" />')
    p_floor = project(-100, 0, 600)
    svg.append(f'<text x="{p_floor[0]:.1f}" y="{p_floor[1]+25:.1f}" font-size="14" font-weight="700" fill="#2a4374" letter-spacing="1">NIVEL SUELO · COTA CERO</text>')
    svg.append('</g>')

    # 2. CABINET CASING (MUEBLE)
    # Left Side Panel: x: 0 to 23, y: 0 to 767, z: 0 to 537
    # Right Side Panel: x: 457 to 480, y: 0 to 767, z: 0 to 537
    # Top Panel: x: 0 to 480, y: 767 to 790, z: 0 to 537
    # Internal Shelf: x: 23 to 457, y: 704 to 727, z: 0 to 530
    svg.append('<g id="cabinet-structure">')
    # Left Side
    svg.append(draw_box(0, 0, 0, 23, 767, 537, stroke="#3a86ff", fill="rgba(58, 134, 255, 0.05)", stroke_width=2))
    # Right Side
    svg.append(draw_box(457, 0, 0, 23, 767, 537, stroke="#3a86ff", fill="rgba(58, 134, 255, 0.05)", stroke_width=2))
    # Top Panel
    svg.append(draw_box(0, 767, 0, 480, 23, 537, stroke="#00f2fe", fill="rgba(0, 242, 254, 0.08)", stroke_width=2.5))
    # Internal Shelf
    svg.append(draw_box(23, 704, 0, 434, 23, 530, stroke="#48cae4", fill="rgba(72, 202, 228, 0.06)", stroke_width=2))
    svg.append('</g>')

    # 3. DREAME BASE STATION & ROBOT (INTERIOR)
    # Base station: width 423, height 568, depth 493 (ramp 153 + body 340).
    # Centered in 434 internal width -> x starts at 23 + (434-423)/2 = 28.5
    # Sits at back: z from 44 to 537 (493 mm depth)
    svg.append('<g id="dreame-station">')
    # Base station body
    svg.append(draw_box(28.5, 0, 44, 423, 568, 493, stroke="#52b788", fill="rgba(82, 183, 136, 0.08)", stroke_width=2, stroke_dash="6,4"))
    # Base station label
    p_base = project(240, 284, 290)
    svg.append(f'<text x="{p_base[0]:.1f}" y="{p_base[1]:.1f}" font-size="16" font-weight="700" fill="#52b788" text-anchor="middle">ESTACIÓN DREAME (423 × 568 × 493 mm)</text>')
    
    # Robot Vacuum docked (350 diameter x 97 height)
    svg.append(draw_box(65, 0, 44, 350, 97, 350, stroke="#74c69d", fill="rgba(116, 198, 157, 0.12)", stroke_width=2))
    p_rob = project(240, 50, 219)
    svg.append(f'<text x="{p_rob[0]:.1f}" y="{p_rob[1]:.1f}" font-size="14" font-weight="700" fill="#74c69d" text-anchor="middle">ROBOT (Ø350 × 97 mm)</text>')
    svg.append('</g>')

    # 4. DOOR WITH SLIDING GUILLOTINE & LINEAR ACTUATOR (OPENED AT 70 DEGREES)
    # The door is hinged at x=0, z=537 (front left edge)
    # Angle theta = 65 degrees open
    # We compute transformed coordinates for the door elements
    door_theta = math.radians(65)
    def door_pt(local_x, local_y, local_t):
        # local_x: 0 to 480 along door surface
        # local_y: 0 to 790 height
        # local_t: 0 to 23 thickness
        # Hinged at (0, 0, 537)
        # rotated around Y axis by door_theta
        # x_world = 0 - local_x * sin(door_theta) + local_t * cos(door_theta)
        # z_world = 537 + local_x * cos(door_theta) + local_t * sin(door_theta)
        xw = 0 - local_x * math.sin(door_theta) + local_t * math.cos(door_theta)
        zw = 537 + local_x * math.cos(door_theta) + local_t * math.sin(door_theta)
        yw = local_y
        return xw, yw, zw

    # Door Frame parts:
    # Door is 480 wide x 790 high.
    # Lower cutout: from local_x = 45 to 435 (width 390), local_y = 0 to 117.
    # So we draw:
    # 1. Left stile: local_x: 0 to 45, y: 0 to 117
    # 2. Right stile: local_x: 435 to 480, y: 0 to 117
    # 3. Main upper door panel: local_x: 0 to 480, y: 117 to 790
    def draw_door_block(lx0, ly0, ldx, ldy, stroke="#ff9e00", fill="rgba(255, 158, 0, 0.08)", stroke_width=2):
        # 8 corners in door local space
        c = [
            project(*door_pt(lx0, ly0, 0)),
            project(*door_pt(lx0 + ldx, ly0, 0)),
            project(*door_pt(lx0 + ldx, ly0 + ldy, 0)),
            project(*door_pt(lx0, ly0 + ldy, 0)),
            project(*door_pt(lx0, ly0, 23)),
            project(*door_pt(lx0 + ldx, ly0, 23)),
            project(*door_pt(lx0 + ldx, ly0 + ldy, 23)),
            project(*door_pt(lx0, ly0 + ldy, 23))
        ]
        faces = [[0,1,2,3], [4,5,6,7], [0,4,7,3], [1,5,6,2], [3,2,6,7], [0,1,5,4]]
        res = []
        for face in faces:
            pts = " ".join([f"{c[i][0]:.1f},{c[i][1]:.1f}" for i in face])
            res.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-linejoin="round" />')
        return "\n".join(res)

    svg.append('<g id="door-assembly">')
    # Left stile (45 x 117)
    svg.append(draw_door_block(0, 0, 45, 117, stroke="#ff9e00", fill="rgba(255, 158, 0, 0.08)"))
    # Right stile (45 x 117)
    svg.append(draw_door_block(435, 0, 45, 117, stroke="#ff9e00", fill="rgba(255, 158, 0, 0.08)"))
    # Main Upper door (480 x 673)
    svg.append(draw_door_block(0, 117, 480, 673, stroke="#ff9e00", fill="rgba(255, 158, 0, 0.08)", stroke_width=2.5))
    
    # Hatch Guides (Rails 20mm on interior face)
    # Left rail: local_x: 25 to 45, y: 0 to 280, local_t: -15 to 0
    # Right rail: local_x: 435 to 455, y: 0 to 280, local_t: -15 to 0
    # Sliding Hatch Panel (410 wide x 140 high) in RAISED position (lifted 130mm up!)
    # Raised y: 117 to 257
    # Hatch thickness: 10mm
    c_hatch = [
        project(*door_pt(35, 120, -10)),
        project(*door_pt(445, 120, -10)),
        project(*door_pt(445, 260, -10)),
        project(*door_pt(35, 260, -10))
    ]
    pts_hatch = " ".join([f"{p[0]:.1f},{p[1]:.1f}" for p in c_hatch])
    svg.append(f'<polygon points="{pts_hatch}" fill="rgba(0, 242, 254, 0.2)" stroke="#00f2fe" stroke-width="2.5" />')
    
    # 12V Linear Actuator
    p_act_bot = project(*door_pt(240, 260, -12))
    p_act_top = project(*door_pt(240, 430, -12))
    svg.append(f'<line x1="{p_act_bot[0]:.1f}" y1="{p_act_bot[1]:.1f}" x2="{p_act_top[0]:.1f}" y2="{p_act_top[1]:.1f}" stroke="#ffffff" stroke-width="6" stroke-linecap="round" />')
    svg.append(f'<line x1="{p_act_bot[0]:.1f}" y1="{p_act_bot[1]:.1f}" x2="{p_act_top[0]:.1f}" y2="{p_act_top[1]:.1f}" stroke="#00f2fe" stroke-width="2" />')
    
    p_door_lbl = project(*door_pt(240, 550, 23))
    svg.append(f'<text x="{p_door_lbl[0]:.1f}" y="{p_door_lbl[1]:.1f}" font-size="16" font-weight="900" fill="#ff9e00" text-anchor="middle">PUERTA SOLAPE TOTAL (480 × 790 mm)</text>')
    
    p_hatch_lbl = project(*door_pt(240, 190, -15))
    svg.append(f'<text x="{p_hatch_lbl[0]:.1f}" y="{p_hatch_lbl[1]:.1f}" font-size="13" font-weight="700" fill="#00f2fe" text-anchor="middle">Compuerta Guillotina (410 × 140 mm)</text>')
    svg.append('</g>')

    # 5. FLOATING 3D TECHNICAL DIMENSION OVERLAYS
    svg.append('<g id="dimensions-3d">')
    # 1. Overall Width: 480 mm across top front
    svg.append(draw_dim_3d((0, 790, 0), (480, 790, 0), "ANCHO MÁXIMO: 480 mm", offset_vec=(0, 60, -30), text_offset=(0, -12)))
    # 2. Overall Height: 790 mm on right side
    svg.append(draw_dim_3d((480, 0, 0), (480, 790, 0), "ALTO MÁXIMO: 790 mm", offset_vec=(70, 0, -30), text_offset=(35, 0)))
    # 3. Overall Depth: 560 mm along right edge
    svg.append(draw_dim_3d((480, 0, 0), (480, 0, 537), "FONDO: 560 mm", offset_vec=(70, 0, 0), text_offset=(30, 15)))
    # 4. Interior Width: 434 mm
    svg.append(draw_dim_3d((23, 680, 100), (457, 680, 100), "ANCHO INTERIOR: 434 mm", offset_vec=(0, 0, 0), stroke="#48cae4", text_color="#48cae4", text_offset=(0, -10)))
    # 5. Tank clearance: 136 mm
    svg.append(draw_dim_3d((457, 568, 200), (457, 704, 200), "DEPÓSITOS: 136 mm LIBRES", offset_vec=(40, 0, 0), stroke="#ff9e00", text_color="#ff9e00", text_offset=(35, 0)))
    # 6. Upper niche: 40 mm
    svg.append(draw_dim_3d((457, 727, 200), (457, 767, 200), "RANURA: 40 mm", offset_vec=(40, 0, 0), stroke="#00f2fe", text_color="#00f2fe", text_offset=(35, 0), font_size=12))
    # 7. Board thickness: 23 mm
    p_thick1 = project(457, 790, 200)
    p_thick2 = project(480, 790, 200)
    svg.append(f'<line x1="{p_thick1[0]:.1f}" y1="{p_thick1[1]:.1f}" x2="{p_thick2[0]:.1f}" y2="{p_thick2[1]:.1f}" stroke="#ff9e00" stroke-width="3" />')
    svg.append(f'<text x="{p_thick2[0]+15:.1f}" y="{p_thick2[1]-15:.1f}" font-size="14" font-weight="700" fill="#ff9e00">Espesor: 23 mm</text>')
    svg.append('</g>')

    # 6. ORTHOGRAPHIC 2D ELEVATIONS (LEFT COLUMN)
    svg.append('''
    <g id="ortho-panel" transform="translate(100, 230)">
      <!-- Panel Background -->
      <rect x="0" y="0" width="460" height="980" rx="8" fill="#131e36" stroke="#2a4374" stroke-width="2" />
      <text x="25" y="40" font-size="18" font-weight="900" fill="#ffffff" letter-spacing="1">SECCIÓN TÉCNICA VERTICAL (1:1)</text>
      <text x="25" y="65" font-size="13" font-weight="600" fill="#00f2fe">DESGLOSE DE COTAS INTERIORES</text>

      <!-- Vertical Scale Bar Diagram -->
      <g transform="translate(40, 100)">
        <!-- Height ruler -->
        <line x1="30" y1="0" x2="30" y2="790" stroke="#2a4374" stroke-width="3" />
        
        <!-- Tapa Superior (767 - 790) -->
        <rect x="60" y="0" width="320" height="23" fill="rgba(0, 242, 254, 0.15)" stroke="#00f2fe" stroke-width="2" />
        <text x="220" y="16" font-size="12" font-weight="700" fill="#00f2fe" text-anchor="middle">TAPA SUPERIOR (23 mm)</text>
        <text x="20" y="16" font-size="12" font-weight="700" fill="#8da2c0" text-anchor="end">790</text>

        <!-- Ranura Recambios (727 - 767) -->
        <rect x="60" y="23" width="320" height="40" fill="rgba(255, 255, 255, 0.03)" stroke="#3a5a8c" stroke-width="1.5" stroke-dasharray="4,3" />
        <text x="220" y="48" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">RANURA RECAMBIOS (40 mm libres)</text>
        <text x="20" y="48" font-size="12" font-weight="700" fill="#8da2c0" text-anchor="end">767</text>

        <!-- Balda Interior (704 - 727) -->
        <rect x="60" y="63" width="320" height="23" fill="rgba(72, 202, 228, 0.15)" stroke="#48cae4" stroke-width="2" />
        <text x="220" y="79" font-size="12" font-weight="700" fill="#48cae4" text-anchor="middle">BALDA INTERIOR (23 mm)</text>
        <text x="20" y="79" font-size="12" font-weight="700" fill="#8da2c0" text-anchor="end">727</text>

        <!-- Espacio Depósitos (568 - 704) -->
        <rect x="60" y="86" width="320" height="136" fill="rgba(255, 158, 0, 0.06)" stroke="#ff9e00" stroke-width="2" stroke-dasharray="5,4" />
        <text x="220" y="150" font-size="15" font-weight="900" fill="#ff9e00" text-anchor="middle">MARGEN EXTRACCIÓN (136 mm)</text>
        <text x="220" y="172" font-size="12" font-weight="600" fill="#ffbd59" text-anchor="middle">Espacio para sacar depósitos de agua</text>
        <text x="20" y="150" font-size="12" font-weight="700" fill="#8da2c0" text-anchor="end">704</text>

        <!-- Torre Dreame (0 - 568) -->
        <rect x="60" y="222" width="320" height="568" fill="rgba(82, 183, 136, 0.08)" stroke="#52b788" stroke-width="2" />
        <text x="220" y="450" font-size="18" font-weight="900" fill="#52b788" text-anchor="middle">ESTACIÓN DREAME</text>
        <text x="220" y="480" font-size="14" font-weight="700" fill="#74c69d" text-anchor="middle">568 mm Altura Oficial</text>
        <text x="220" y="505" font-size="12" font-weight="500" fill="#95d5b2" text-anchor="middle">(Ancho: 423 mm | Fondo: 493 mm)</text>
        <text x="20" y="228" font-size="12" font-weight="700" fill="#8da2c0" text-anchor="end">568</text>

        <!-- Suelo -->
        <line x1="10" y1="790" x2="390" y2="790" stroke="#ffffff" stroke-width="3" />
        <text x="20" y="795" font-size="12" font-weight="700" fill="#ffffff" text-anchor="end">0</text>
        <text x="220" y="815" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">SUELO / COTA CERO</text>
      </g>
    </g>
    ''')

    # 7. SUMMARY SPECS TABLE BLOCK (BOTTOM RIGHT)
    svg.append('''
    <g id="specs-block" transform="translate(1620, 1050)">
      <rect x="0" y="0" width="840" height="470" rx="8" fill="#131e36" stroke="#2a4374" stroke-width="2" />
      <text x="35" y="45" font-size="22" font-weight="900" fill="#ffffff" letter-spacing="1">RESUMEN DE COTAS &amp; AJUSTES MILIMÉTRICOS</text>
      
      <g transform="translate(35, 75)" font-size="14" font-weight="600">
        <!-- Row 1 -->
        <rect x="0" y="0" width="770" height="42" fill="#1a2949" rx="4" />
        <text x="20" y="26" fill="#8da2c0">Ancho Total Exterior (Mínimo Estricto):</text>
        <text x="750" y="26" fill="#00f2fe" font-weight="800" text-anchor="end">480 mm</text>
        
        <!-- Row 2 -->
        <rect x="0" y="50" width="770" height="42" fill="#15213b" rx="4" />
        <text x="20" y="76" fill="#8da2c0">Alto Total Exterior (Límite Máximo):</text>
        <text x="750" y="76" fill="#00f2fe" font-weight="800" text-anchor="end">790 mm</text>
        
        <!-- Row 3 -->
        <rect x="0" y="100" width="770" height="42" fill="#1a2949" rx="4" />
        <text x="20" y="126" fill="#8da2c0">Fondo Total Exterior:</text>
        <text x="750" y="126" fill="#00f2fe" font-weight="800" text-anchor="end">560 mm</text>
        
        <!-- Row 4 -->
        <rect x="0" y="150" width="770" height="42" fill="#15213b" rx="4" />
        <text x="20" y="176" fill="#8da2c0">Vano Robot Puerta (Cota Cero):</text>
        <text x="750" y="176" fill="#ff9e00" font-weight="800" text-anchor="end">390 × 117 mm</text>
        
        <!-- Row 5 -->
        <rect x="0" y="200" width="770" height="42" fill="#1a2949" rx="4" />
        <text x="20" y="226" fill="#8da2c0">Montantes Laterales de la Puerta:</text>
        <text x="750" y="226" fill="#ff9e00" font-weight="800" text-anchor="end">45 mm / lado</text>

        <!-- Row 6 -->
        <rect x="0" y="250" width="770" height="42" fill="#15213b" rx="4" />
        <text x="20" y="276" fill="#8da2c0">Holgura Rieles Interior (20mm Riel vs Lateral):</text>
        <text x="750" y="276" fill="#48cae4" font-weight="800" text-anchor="end">2.0 mm libre (Cero Fricción)</text>

        <!-- Row 7 -->
        <rect x="0" y="300" width="770" height="42" fill="#1a2949" rx="4" />
        <text x="20" y="326" fill="#8da2c0">Holgura Lateral Estación Base (423mm en 434mm):</text>
        <text x="750" y="326" fill="#52b788" font-weight="800" text-anchor="end">5.5 mm libre / lado</text>

        <!-- Row 8 -->
        <rect x="0" y="350" width="770" height="42" fill="#15213b" rx="4" />
        <text x="20" y="376" fill="#8da2c0">Espacio Libre Extracción Depósitos Agua:</text>
        <text x="750" y="376" fill="#52b788" font-weight="800" text-anchor="end">136 mm libres (Cumple norma)</text>
      </g>
    </g>
    ''')

    svg.append('</svg>')
    
    svg_content = "\n".join(svg)
    svg_path = "/Users/jorge/projects/mueble-aspiradora/render_mueble_wireframe.svg"
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("SVG saved to:", svg_path)
    
    # Render to high-res PNG using qlmanage
    png_tmp_dir = "/tmp/render_wireframe"
    os.makedirs(png_tmp_dir, exist_ok=True)
    subprocess.run(["qlmanage", "-t", "-s", "2560", "-o", png_tmp_dir, svg_path], check=True)
    
    rendered_png = os.path.join(png_tmp_dir, "render_mueble_wireframe.svg.png")
    final_png = "/Users/jorge/projects/mueble-aspiradora/render_mueble_wireframe.png"
    final_jpg = "/Users/jorge/projects/mueble-aspiradora/render_mueble_wireframe.jpg"
    
    # Convert and optimize via PIL
    im = Image.open(rendered_png)
    im = im.convert("RGB")
    im.save(final_png, "PNG")
    im.save(final_jpg, "JPEG", quality=95)
    print("Saved high-res PNG & JPG:", final_jpg)

if __name__ == "__main__":
    generate_blueprint()
