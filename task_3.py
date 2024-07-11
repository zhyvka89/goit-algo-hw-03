
def hanoi(n, hanoi_towers, source, target, auxiliary):
    if n <= 0:
      raise ValueError("The number of disks must be a positive integer.")
    if n == 1:
      move_disk(source, target, hanoi_towers)
    else:
      hanoi(n-1, hanoi_towers, source, auxiliary, target)
      move_disk(source, target, hanoi_towers)
      hanoi(n-1, hanoi_towers, auxiliary, target, source)
    

def move_disk(source, target, hanoi_towers):
  disk = hanoi_towers[source].pop()
  hanoi_towers[target].append(disk)
  print(f"Перемістити диск з {source} на {target}: {disk}")
  print(f"Проміжний стан: {hanoi_towers}")


def main():
  try:
    n = int(input("Введіть кількість дисків: "))

    disks = [i for i in range(1, n+1)]
    disks.reverse()

    hanoi_towers = {
      "A": disks,
      "B": [],
      "C": []
    }

    if n > 0:
      print(f'Початковий стан: {hanoi_towers}')

    hanoi(n, hanoi_towers, 'A', 'C', 'B')
    print(f'Кінцевий стан стан: {hanoi_towers}')
  except Exception as e:
    print(e)


if __name__ == "__main__":
  main()