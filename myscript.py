import os
from demo_test_dpsr_real import main
base_dir = '/home/hessesummer/Caltec-UCSDbirds-200-2011/CUB_200_2011'


def prepare_folder():
    # grandparent folder
    grandparents = ['images_x2', 'images_x4']
    for grandparent in grandparents:
        grandparent = os.path.join(base_dir, grandparent)
        if not os.path.exists(grandparent):
            os.mkdir(grandparent)

        # parent folder
        for parent in os.listdir(os.path.join(base_dir, 'images')):
            parent = os.path.join(grandparent, parent)
            if not os.path.exists(parent):
                os.mkdir(parent)


def get_allimgnames():
    """获得所有图片列表"""
    img_name_list = []
    with open(os.path.join(base_dir, 'images.txt')) as f:
        for line in f:
            img_name_list.append(line[:-1].split(' ')[-1])
    return img_name_list


if __name__ == '__main__':
    prepare_folder()
    img_name_list = get_allimgnames()
    # x2
    for img_name in img_name_list:
        print(img_name)
        main(2, base_dir, 'images', 'images_x2', img_name)
    # x4
    for img_name in img_name_list:
        main(4, base_dir, 'images', 'images_x4', img_name)



