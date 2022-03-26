from numpy import mat


def show_gpu_menu():
    print(
        "------------------------------------------------------\n"
       +"|                |Graphics Card Menu|                |\n"
       +"|----------------------------------------------------|\n"
       +"|1-Check a specific Graphic Card benchmarks:         |\n"
       +"|----------------------------------------------------|\n"
       +"|2-Check a specific Graphic Card price               |\n"
       +"|----------------------------------------------------|\n"
       +"|3-Recommended FPS per dollar Graphic Card           |\n"
       +"|----------------------------------------------------|\n"
    )
    ch=input()
    def f(ch):
        match ch:
            case '1': print("1")
            case '2': print("2")
            case '3': print("3")