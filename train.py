from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')
    results = model.train(
        data='dataset/data.yaml', 
        epochs=10,
        imgsz=640,
        batch=8,
        name='car_damage_train'
    )

if __name__ == '__main__':
    main()
