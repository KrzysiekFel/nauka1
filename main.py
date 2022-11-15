
print(__name__)
from speed.calculation import calculate_speed

def start_script():
    dis_value = int(input("Podaj wartosc ile km przebiegles: "))
    tim_value = int(input("Podaj wartość w ciągu ilu godz przebiegłeś ten dystans: "))
    speed = calculate_speed(distance=dis_value, time=tim_value)
    print(f"Przebiegles z predkoscia {speed:.2f} km/h")

if __name__ == "__main__":
    start_script()