
import argparse
import pymeshlab as ml

#Target number of vertex
TARGET=100000

argParser = argparse.ArgumentParser(description='Reduces number of faces to a desired number. Default is {}. Supported input file formats: PLY, STL, OFF, OBJ, 3DS, VRML 2.0, X3D and COLLADA. '.format(TARGET))
argParser.add_argument('input', help='path to input file')
argParser.add_argument('output', help='path to output file')
argParser.add_argument('--target', metavar='N', type=int, default=TARGET, help='an integer for the desired number of faces')

args = argParser.parse_args()

if (args.target > 0 and TARGET != args.target):
    TARGET = args.target

ms = ml.MeshSet()
print('Loading input file...')
ms.load_new_mesh(args.input)
m = ms.current_mesh()
print('Input mesh has', m.face_number(), 'faces. Target is', TARGET)
print('Starting decimation...')

if (ms.current_mesh().vertex_number() > TARGET):
    ms.apply_filter('simplification_quadric_edge_collapse_decimation', targetfacenum=TARGET, preservenormal=True)
    print("Decimated to", m.face_number(), 'faces.')
else:
    print('No action taken. Mesh already below a target.')

ms.save_current_mesh(args.output)
