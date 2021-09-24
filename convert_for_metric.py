import glob

'''
This short script convertes my used yolov5 bounding boxes for the metric tool.
It converts the classes with id 2 to id 0 (car) and the classes with id 4 to 1 (pedestrian)
Predicted Bounding Boxes contain a confidence value for each detection, so if you want to convert predicted
bounding boxes set confidence to True otherwise to false
The script also changes the format from
<class id><left><top><width><heigt><confidence> to <class id><confidence><left><top><width><heigt>
'''

# Do the bounding box files contain a confidence
confidence = True
# Folder who contains the predicted or ground-truth bounding boxes
file_list = glob.glob('/media/jan/TEST/_Masterarbeit/metrics/carla_rendered/gt_before/*.txt')

# Output Folder for converted bounding boxes
out_folder = '/media/jan/TEST/_Masterarbeit/metrics/carla_rendered/gt/'

for file in file_list:
    with open(file) as f:
        content = f.readlines()
    data_str = ''
    file_name = file.split('/')[-1]
    with open(out_folder + file_name, 'a') as outfile:
        for line in content:
            input_class = int(line.split()[0])
            if input_class == 2:
                output_class = 0
                x = line.split()[1]
                y = line.split()[2]
                w = line.split()[3]
                h = line.split()[4]
                if confidence:
                    c = line.split()[5]
                    outfile.write(f"{output_class} {c} {x} {y} {w} {h} \n")
                else:
                    outfile.write(f"{output_class} {x} {y} {w} {h} \n")
            elif input_class == 4:
                output_class = 1
                x = line.split()[1]
                y = line.split()[2]
                w = line.split()[3]
                h = line.split()[4]
                if confidence:
                    c = line.split()[5]
                    outfile.write(f"{output_class} {c} {x} {y} {w} {h} \n")
                else:
                    outfile.write(f"{output_class} {x} {y} {w} {h} \n")
    outfile.close()
