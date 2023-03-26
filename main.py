from augs.photos_rotation import data_transforms
from dataset import SimpleDataset
from show.same_img import show


def main():

    ds = SimpleDataset('images/people', transforms=data_transforms)
    show(nrows=3, ncols=4, ds=ds, img_idx=0)


if __name__ == '__main__':

    main()