import csv

class Toolkit:
    def tryToCleanOrReturnBlank(str):
        try:
            result = str.getText().strip()
        except:
            result = ""
        return result

    def fileWriter(file, fieldnames, data):
        with open(file, "w+", encoding="UTF8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)