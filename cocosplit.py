import json
from pycocotools.coco import COCO

if __name__ == "__main__":
    annotation_file = r"G:\study\原型网络\Prototypical-Networks-for-image-classification\omniglot\dataset2\train_.json"
    with open(annotation_file, "r") as f:
        dataset = json.load(f)
    coco = COCO(annotation_file=annotation_file)
    '''
    根据categories,将每个json文件存放10个类别
    新的dataset需要修改 => images,annotation,categories
    '''
    images_set = set()
    images_new = []
    annotation_new = []
    categories_new = []
    target_categories = [x for x in range(1, 11)]
    for ann in dataset['annotations']:
        if ann['category_id'] in target_categories:
            annotation_new.append(ann)
            images_set.add(ann['image_id'])
    for img_id in images_set:
        images = dataset['images']
        images_new.append(images[img_id])
    for category in dataset['categories']:
        if category['id'] in target_categories:
            categories_new.append(category)
    # for i in range(10):
    #     categories = dataset['categories']
    #     category = categories[i]

    #     category_id = category['id']
    #     categories_new.append(category)
    #     images = coco.catToImgs[category_id]
    #     for image in images:  # img的id
    #         img = dataset['images'][image]
    #         images_new.append(img)

    #         annotations = coco.imgToAnns[image]
    #         annotation_new += annotations

    dataset['images'] = images_new
    dataset['annotations'] = annotation_new
    dataset['categories'] = categories_new

    save_file = r"G:\study\coco\train.json"
    with open(save_file, 'wt', encoding='UTF-8') as coco:
        json.dump(dataset, coco, ensure_ascii=False)

    # print(dataset)
