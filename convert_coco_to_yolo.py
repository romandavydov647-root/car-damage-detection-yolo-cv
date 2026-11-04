import json
import os
import shutil

def convert_coco_to_yolo(json_path, images_dir, output_dir, limit=None):
    os.makedirs(f"{output_dir}/images/train", exist_ok=True)
    os.makedirs(f"{output_dir}/labels/train", exist_ok=True)

    print(f"Загружаем JSON: {json_path}")
    with open(json_path, 'r') as f:
        data = json.load(f)

    images_info = {img['id']: (img['width'], img['height'], img['file_name']) for img in data['images']}
    annotations_by_image = {}
    for ann in data['annotations']:
        img_id = ann['image_id']
        if img_id not in annotations_by_image:
            annotations_by_image[img_id] = []
        annotations_by_image[img_id].append(ann)

    images_to_process = list(images_info.items())
    if limit:
        images_to_process = images_to_process[:limit]
    
    print(f"Обрабатываем {len(images_to_process)} картинок...")

    for img_id, (img_w, img_h, file_name) in images_to_process:
        src_img = os.path.join(images_dir, file_name)
        dst_img = os.path.join(f"{output_dir}/images/train", file_name)
        if os.path.exists(src_img):
            shutil.copy(src_img, dst_img)

        txt_name = os.path.splitext(file_name)[0] + '.txt'
        txt_path = os.path.join(f"{output_dir}/labels/train", txt_name)
        
        lines = []
        if img_id in annotations_by_image:
            for ann in annotations_by_image[img_id]:
                cat_id = ann['category_id'] - 1 
                x_min, y_min, w, h = ann['bbox']
                
                x_center = (x_min + w / 2) / img_w
                y_center = (y_min + h / 2) / img_h
                w_norm = w / img_w
                h_norm = h / img_h
                
                lines.append(f"{cat_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}")
        
        with open(txt_path, 'w') as f:
            f.write('\n'.join(list(set(lines))))

    print("Конвертация завершена!")

if __name__ == "__main__":
    # Пример запуска (пути нужно будет поменять под себя)
    # convert_coco_to_yolo("annotations/instances_train2017.json", "train2017", "dataset", limit=1000)
    print("Скрипт готов к использованию.")
