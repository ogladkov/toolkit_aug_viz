import albumentations as A


data_transforms = A.Compose([
    A.Resize(height=224, width=224),
    A.ShiftScaleRotate(shift_limit=0.4,
                       rotate_limit=(-25, 25), border_mode=0,
                       shift_limit_x=0.2,
                       shift_limit_y=0.2),
    A.RandomBrightnessContrast(brightness_limit=0.5, contrast_limit=0.6, p=0.3),
    A.ColorJitter(p=0.1),
    A.HueSaturationValue(hue_shift_limit=(-30, 30),
                         sat_shift_limit=(-180, 50),
                         val_shift_limit=0,
                         p=0.5),
    A.RandomToneCurve(p=0.3),
    A.OneOf([A.MedianBlur(blur_limit=11, p=0.5),
             A.GaussianBlur(blur_limit=11, p=0.5)], p=0.15),
    A.ImageCompression(quality_lower=65, p=0.25),
    A.Perspective(p=0.5),
],
    p=1.0)