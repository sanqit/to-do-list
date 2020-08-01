class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


for instance in [Angel(), Demon()]:
    print(instance.color, instance.feature, instance.home, sep='\n')
