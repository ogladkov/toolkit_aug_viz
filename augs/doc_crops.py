import albumentations as A


data_transforms = A.Compose([
    # A.Resize(height=224, width=224),
    A.RGBShift(b_shift_limit=(-20, 20), always_apply=1),
    A.ShiftScaleRotate(scale_limit=(-0.4, 0.4),
                       rotate_limit=0, border_mode=0,
                       shift_limit_x=0.25,
                       shift_limit_y=0.25),
    A.RandomBrightnessContrast(brightness_limit=0.35, contrast_limit=0.6, p=0.3),
    A.HueSaturationValue(hue_shift_limit=(-30, 30),
                         sat_shift_limit=0,
                         val_shift_limit=0,
                         p=0.5),
    # A.RandomToneCurve(p=0.3),
    # A.OneOf([A.MedianBlur(blur_limit=5, p=0.5),
    #          A.GaussianBlur(blur_limit=5, p=0.5)], p=0.15),
    # A.ImageCompression(quality_lower=65, p=0.25),
    # A.Perspective(p=0.5),
],
    p=1.0)