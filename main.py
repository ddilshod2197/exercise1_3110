class Kompyuter:
    def __init__(self, model, ram, disk_hajmi):
        self.model = model
        self.ram = ram
        self.disk_hajmi = disk_hajmi

    def malumot(self):
        return f"Model: {self.model}, RAM: {self.ram} GB, Disk hajmi: {self.disk_hajmi} GB"

    def ram_yangila(self, yangi_ram):
        self.ram = yangi_ram
        print(f"RAM yangilandi: {self.ram} GB")


komp1 = Kompyuter("Dell Inspiron", 8, 512)
print(komp1.malumot())

komp1.ram_yangila(16)
print(komp1.malumot())
