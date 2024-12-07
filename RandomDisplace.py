bl_info = {
    "name": "Displacer",
    "author": "mupgarlic - N.T. Studio",
    "version": (1, 0),
    "blender": (4, 0, 2),
    "location": "3D Viewport > Sidebar > N.T. Studio",
    "description": "Create random noise textures for the 'Displace' modifier",
    "category": "Development",
}

import bpy
import random

#/// HIGH POLY PLANE ///#
class planeOperator(bpy.types.Operator):
    """Add a high poly plane"""
    bl_idname = "object.plane_operator"
    bl_label = "Add a high poly plane"
    
    def execute(self, context):
      
        #Add a plane
        bpy.ops.mesh.primitive_plane_add()
        
        #Subdivide in Edit mode
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.subdivide(number_cuts=150)
        bpy.ops.object.editmode_toggle()
        
        return {'FINISHED'}

#/// HIGH POLY CUBE ///#
class cubeOperator(bpy.types.Operator):
    """Add a high poly cube"""
    bl_idname = "object.cube_operator"
    bl_label = "Add a high poly cube"
    
    def execute(self, context):
      
        #Add a cube
        bpy.ops.mesh.primitive_cube_add()
        
        #Subdivide in Edit mode
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.subdivide(number_cuts=150)
        bpy.ops.object.editmode_toggle()
        
        return {'FINISHED'}
        
#/// HIGH POLY ICO SPHERE ///#
class icoOperator(bpy.types.Operator):
    """Add a high poly Ico Sphere"""
    bl_idname = "object.ico_operator"
    bl_label = "Add a high poly Ico Sphere"
    
    def execute(self, context):
      
        #Add an Icosphere
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=8)
        
        return {'FINISHED'}


#/// CREATE THE DISPLACE ///#
class displOperator(bpy.types.Operator):
    """Add a Displace modifier with random noise"""
    bl_idname = "object.displ_operator"
    bl_label = "Add the Displace modifier"
    
    def execute(self, context):
      
        #Set object mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        #Make sure to clean any 'Displace' thing on the object
        bpy.ops.object.modifier_remove(modifier="Displace")
        
        #Add a new 'Displace' modifier
        bpy.ops.object.modifier_add(type='DISPLACE')
        
        #Set a random strength for the modifier
        bpy.context.object.modifiers["Displace"].strength = random.random()
        
        #Create a new texture
        tex = [
            'BLEND', 'CLOUDS', 'DISTORTED_NOISE', 'MAGIC',
            'MARBLE', 'MUSGRAVE', 'NOISE', 'STUCCI', 'VORONOI', 'WOOD'
        ]
        
        res = random.choice(tex)
       
        bpy.data.textures.new(name="Noise Rand", type=res)
        bpy.context.object.modifiers["Displace"].texture = bpy.data.textures['Noise Rand']
        
        #/// RANDOM NOISE TEXTURES ///#
        
        #If texture = Blend
        if res == 'BLEND':
            
            #Set tex progression
            prog = [
                'LINEAR', 'QUADRATIC', 'EASING', 'RADIAL',
                'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE'
            ]
            
            bpy.data.textures["Noise Rand"].progression = random.choice(prog)
                
            #Set tex orientation
            if prog == 'LINEAR' or 'QUADRATIC' or 'EASING' or 'RADIAL':
                flip = ['HORIZONTAL', 'VERTICAL']
                
                bpy.data.textures["Noise Rand"].use_flip_axis = random.choice(flip)
                
        #If texture = Clouds
        if res == 'CLOUDS':
            
            #Set noise basis
            basis = [
                'BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN',
                'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4',
                'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'
            ]
            
            bpy.data.textures["Noise Rand"].noise_basis = random.choice(basis)
            
            #Set type
            clouds_type = ['SOFT_NOISE', 'HARD_NOISE']
            bpy.data.textures["Noise Rand"].noise_type = random.choice(clouds_type)
            
            #Set if colored or not
            clouds_color = ['GRAYSCALE', 'COLOR']
            bpy.data.textures["Noise Rand"].cloud_type = random.choice(clouds_color)
            
            #Set scale, depth & nabla
            bpy.data.textures["Noise Rand"].noise_scale = random.uniform(0, 2)
            bpy.data.textures["Noise Rand"].noise_depth = random.randint(0, 24)
            bpy.data.textures["Noise Rand"].nabla = random.uniform(0.001, 0.1)
        
        #If texture = Distorted Noise
        if res == 'DISTORTED_NOISE':
            
            #Set noise basis & distortion
            basis_dist = [
                'BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN',
                'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4',
                'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'
            ]
            
            bpy.data.textures["Noise Rand"].noise_basis = random.choice(basis_dist)
            bpy.data.textures["Noise Rand"].noise_distortion = random.choice(basis_dist)
            
            #Set amount, scale & nabla
            bpy.data.textures["Noise Rand"].distortion = random.uniform(0, 10)
            bpy.data.textures["Noise Rand"].noise_scale = random.uniform(0, 2)
            bpy.data.textures["Noise Rand"].nabla = random.uniform(0.001, 0.1)
            
        #If texture = Magic
        if res == 'MAGIC':
            
            #Set depth & turbulence
            bpy.data.textures["Noise Rand"].noise_depth = random.randint(0, 24)
            bpy.data.textures["Noise Rand"].turbulence = random.uniform(3, 15)
            
        #If texture = Marble
        if res == 'MARBLE':
            
            #Set noise basis
            basis_dist = [
                'BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN',
                'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4',
                'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'
            ]
            
            bpy.data.textures["Noise Rand"].noise_basis = random.choice(basis_dist)
            
            #Set pattern
            patt = ['SOFT', 'SHARP', 'SHARPER']
            bpy.data.textures["Noise Rand"].marble_type = random.choice(patt)
            
            #Set second basis & type
            bas2 = ['SIN', 'SAW', 'TRI']
            bpy.data.textures["Noise Rand"].noise_basis_2 = random.choice(bas2)
            
            marb_type = ['SOFT_NOISE', 'HARD_NOISE']
            bpy.data.textures["Noise Rand"].noise_type = random.choice(marb_type)
            
            #Set scale, depth, turbulence & nabla
            bpy.data.textures["Noise Rand"].noise_scale = random.uniform(0, 2)
            bpy.data.textures["Noise Rand"].noise_depth = random.randint(0, 24)
            bpy.data.textures["Noise Rand"].turbulence = random.uniform(0, 200)
            bpy.data.textures["Noise Rand"].nabla = random.uniform(0.001, 0.1)
            
        #If texture = Musgrave
        if res == 'MUSGRAVE':
            
            #Set noise basis
            basis = [
                'BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN',
                'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4',
                'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'
            ]
            
            bpy.data.textures["Noise Rand"].noise_basis = random.choice(basis)
            
            #Set type
            musg = [
                'MULTIFRACTAL', 'RIDGED_MULTIFRACTAL',
                'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'
            ]
            
            musg_res = random.choice(musg)
            
            bpy.data.textures["Noise Rand"].musgrave_type = musg_res
            
            #Modify the settings depending on its type
            if musg_res == 'MULTIFRACTAL' or 'FBM':
                bpy.data.textures["Noise Rand"].noise_scale = random.uniform(0, 2)
                bpy.data.textures["Noise Rand"].nabla = random.uniform(0.001, 0.1)
                bpy.data.textures["Noise Rand"].dimension_max = random.uniform(0.0001, 2)
                bpy.data.textures["Noise Rand"].lacunarity = random.uniform(0.01, 6)
                bpy.data.textures["Noise Rand"].octaves = random.uniform(0.01, 8)
                bpy.data.textures["Noise Rand"].noise_intensity = random.uniform(0.02, 10)
                
            if musg_res == 'RIDGED_MULTIFRACTAL' or 'HYBRID_MULTIFRACTAL':
                bpy.data.textures["Noise Rand"].noise_scale = random.uniform(0, 2)
                bpy.data.textures["Noise Rand"].nabla = random.uniform(0.001, 0.1)
                bpy.data.textures["Noise Rand"].dimension_max = random.uniform(0.0001, 2)
                bpy.data.textures["Noise Rand"].lacunarity = random.uniform(0.01, 6)
                bpy.data.textures["Noise Rand"].octaves = random.uniform(0.01, 8)
                bpy.data.textures["Noise Rand"].offset = random.uniform(1, 6)
                bpy.data.textures["Noise Rand"].noise_intensity = random.uniform(0.02, 10)
                bpy.data.textures["Noise Rand"].gain = random.uniform(0.01, 6)
                
            if musg_res == 'HETERO_TERRAIN':
                bpy.data.textures["Noise Rand"].noise_scale = random.uniform(0, 2)
                bpy.data.textures["Noise Rand"].nabla = random.uniform(0.001, 0.1)
                bpy.data.textures["Noise Rand"].dimension_max = random.uniform(0.0001, 2)
                bpy.data.textures["Noise Rand"].lacunarity = random.uniform(0.01, 6)
                bpy.data.textures["Noise Rand"].octaves = random.uniform(0.01, 8)
                bpy.data.textures["Noise Rand"].offset = random.uniform(1, 6)
                bpy.data.textures["Noise Rand"].noise_intensity = random.uniform(0.02, 10)
                
        #If texture = Stucci
        if res == 'STUCCI':
            
            #Set noise basis
            basis = [
                'BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN',
                'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4',
                'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'
            ]
            
            bpy.data.textures["Noise Rand"].noise_basis = random.choice(basis)
            
            #Set pattern
            stuc_pattern = ['PLASTIC', 'WALL_IN', 'WALL_OUT']
            bpy.data.textures["Noise Rand"].stucci_type = random.choice(stuc_pattern)
            
            #Set type
            stuc_type = ['SOFT_NOISE', 'HARD_NOISE']
            bpy.data.textures["Noise Rand"].noise_type = random.choice(stuc_type)
            
            #Set scale & turbulence
            bpy.data.textures["Noise Rand"].noise_scale = random.uniform(0, 2)
            bpy.data.textures["Noise Rand"].turbulence = random.uniform(0, 200)
            
        #If texture = Voronoi
        if res == 'VORONOI':
            
            #Set distance
            distance = [
                'DISTANCE', 'DISTANCE_SQUARED', 'MANHATTAN', 'CHEBYCHEV',
                'MINKOVSKY_HALF', 'MINKOVSKY_FOUR', 'MINKOVSKY'
            ]
            
            pick_dist = random.choice(distance)
            
            bpy.data.textures["Noise Rand"].distance_metric = pick_dist
            
            #Set exponent if need it
            if pick_dist == 'MINKOVSKY':
                bpy.data.textures["Noise Rand"].minkovsky_exponent = random.uniform(0.2, 10)
                
            #Set coloring
            coloring = ['INTENSITY', 'POSITION', 'POSITION_OUTLINE', 'POSITION_OUTLINE_INTENSITY']
            bpy.data.textures["Noise Rand"].color_mode = random.choice(coloring)
            
            #Set intensity, scale & nabla
            bpy.data.textures["Noise Rand"].noise_intensity = random.uniform(0.02, 10)
            bpy.data.textures["Noise Rand"].noise_scale = random.uniform(0, 2)
            bpy.data.textures["Noise Rand"].nabla = random.uniform(0.001, 0.1)
        
            #Set feature weights
            bpy.data.textures["Noise Rand"].weight_1 = random.uniform(-2, 2)
            bpy.data.textures["Noise Rand"].weight_2 = random.uniform(-2, 2)
            bpy.data.textures["Noise Rand"].weight_3 = random.uniform(-2, 2)
            bpy.data.textures["Noise Rand"].weight_4 = random.uniform(-2, 2)
        
        #If texture = Wood
        if res == 'WOOD':
            
            #Set noise basis
            basis = [
                'BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN',
                'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4',
                'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'
            ]
            
            bpy.data.textures["Noise Rand"].noise_basis = random.choice(basis)
            
            #Set wood pattern
            wood_patt = ['BANDS', 'RINGS', 'BANDNOISE', 'RINGNOISE']
            bpy.data.textures["Noise Rand"].wood_type = random.choice(wood_patt)
            
            #Set second basis & type
            bas2 = ['SIN', 'SAW', 'TRI']
            bpy.data.textures["Noise Rand"].noise_basis_2 = random.choice(bas2)
            
            #Set scale, turbulence & nabla
            bpy.data.textures["Noise Rand"].noise_scale = random.uniform(0, 2)
            bpy.data.textures["Noise Rand"].turbulence = random.uniform(0, 200)
            bpy.data.textures["Noise Rand"].nabla = random.uniform(0.001, 0.1)
        
        #Modify the texture's colors
        bpy.data.textures["Noise Rand"].intensity = random.uniform(1, 2) #Brightness
        bpy.data.textures["Noise Rand"].contrast = random.uniform(1, 5) #Contrast
        bpy.data.textures["Noise Rand"].saturation = random.uniform(0, 2) #Saturation
        
        return {'FINISHED'}


class texCleanOperator(bpy.types.Operator):
    """Delete any extra Noise Texture"""
    bl_idname = "object.noise_operator"
    bl_label = "Delete any extra noise texture"
    
    def execute(self, context):
        
        d = bpy.data.textures['Noise Rand']
        bpy.data.textures.remove(d)
        
        return {'FINISHED'}

class VIEW3D_PT_my_custom_panel(bpy.types.Panel):  #Class naming convention ‘CATEGORY_PT_name’

    #Where to add the panel in the UI
    bl_space_type = "VIEW_3D"  #3D Viewport area
    bl_region_type = "UI"  #Sidebar region
    
    #Add labels
    bl_category = "N.T. Studio"  #Found in the Sidebar
    bl_label = "Displacer"  #Found at the top of the Panel

    def draw(self, context):
        """define the layout of the panel"""
        row = self.layout.row()
        row.operator("object.plane_operator", text="High poly plane")
        
        row = self.layout.row()
        row.operator("object.cube_operator", text="High poly cube")
        
        row = self.layout.row()
        row.operator("object.ico_operator", text="High poly sphere")
        
        self.layout.separator()
        
        row = self.layout.row()
        row.operator("object.displ_operator", text="Add 'Displace'")
        
        row = self.layout.row()
        row.operator("object.noise_operator", text="Please, delete texture")


def register():
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)
    bpy.utils.register_class(planeOperator)
    bpy.utils.register_class(cubeOperator)
    bpy.utils.register_class(icoOperator)
    bpy.utils.register_class(displOperator)
    bpy.utils.register_class(texCleanOperator)


def unregister():
    bpy.utils.unregister_class(texCleanOperator)
    bpy.utils.unregister_class(displOperator)
    bpy.utils.unregister_class(icoOperator)
    bpy.utils.unregister_class(cubeOperator)
    bpy.utils.unregister_class(planeOperator)
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)


if __name__ == "__main__":
    register()