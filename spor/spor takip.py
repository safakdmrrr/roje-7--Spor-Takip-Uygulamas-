import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox


class Sporcu:
    def __init__(self, ad, spor_dali):
        self.ad = ad
        self.spor_dali = spor_dali
        self.antrenmanlar = []

    def program_olustur(self, ad, detaylar):
        antrenman = {"ad": ad, "detaylar": detaylar, "ilerleme": None}
        self.antrenmanlar.append(antrenman)

    def ilerleme_kaydet(self, antrenman_adı, ilerleme):
        for antrenman in self.antrenmanlar:
            if antrenman["ad"] == antrenman_adı:
                antrenman["ilerleme"] = ilerleme
                return True
        return False

    def rapor_al(self):
        rapor = f"{self.ad} adlı sporcunun raporu:\n"
        for antrenman in self.antrenmanlar:
            rapor += f"{antrenman['ad']}: {antrenman['ilerleme']}\n"
        return rapor


class Takip:
    def __init__(self):
        self.sporcular = []

    def sporcu_ekle(self, sporcu):
        self.sporcular.append(sporcu)

    def sporcu_bul(self, ad):
        for sporcu in self.sporcular:
            if sporcu.ad == ad:
                return sporcu
        return None


class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.takip = Takip()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Sporcu Ekle
        layout_sporcu_ekle = QHBoxLayout()
        lbl_sporcu_ad = QLabel("Sporcu Adı:")
        self.input_sporcu_ad = QLineEdit()
        lbl_sporcu_dal = QLabel("Spor Dalı:")
        self.input_sporcu_dal = QLineEdit()
        btn_sporcu_ekle = QPushButton("Sporcu Ekle")
        btn_sporcu_ekle.clicked.connect(self.sporcu_ekle)
        layout_sporcu_ekle.addWidget(lbl_sporcu_ad)
        layout_sporcu_ekle.addWidget(self.input_sporcu_ad)
        layout_sporcu_ekle.addWidget(lbl_sporcu_dal)
        layout_sporcu_ekle.addWidget(self.input_sporcu_dal)
        layout_sporcu_ekle.addWidget(btn_sporcu_ekle)
        layout.addLayout(layout_sporcu_ekle)

        # Program Oluştur
        layout_program_olustur = QHBoxLayout()
        lbl_sporcu_ad2 = QLabel("Sporcu Adı:")
        self.input_sporcu_ad2 = QLineEdit()
        lbl_antrenman_ad = QLabel("Antrenman Adı:")
        self.input_antrenman_ad = QLineEdit()
        lbl_antrenman_detay = QLabel("Antrenman Detayları:")
        self.input_antrenman_detay = QLineEdit()
        btn_program_olustur = QPushButton("Program Oluştur")
        btn_program_olustur.clicked.connect(self.program_olustur)
        layout_program_olustur.addWidget(lbl_sporcu_ad2)
        layout_program_olustur.addWidget(self.input_sporcu_ad2)
        layout_program_olustur.addWidget(lbl_antrenman_ad)
        layout_program_olustur.addWidget(self.input_antrenman_ad)
        layout_program_olustur.addWidget(lbl_antrenman_detay)
        layout_program_olustur.addWidget(self.input_antrenman_detay)
        layout_program_olustur.addWidget(btn_program_olustur)
        layout.addLayout(layout_program_olustur)

        # İlerleme Kaydet
        layout_ilerleme_kaydet = QHBoxLayout()
        lbl_sporcu_ad3 = QLabel("Sporcu Adı:")
        self.input_sporcu_ad3 = QLineEdit()
        lbl_antrenman_ad2 = QLabel("Antrenman Adı:")
        self.input_antrenman_ad2 = QLineEdit()
        lbl_ilerleme = QLabel("İlerleme:")
        self.input_ilerleme = QLineEdit()
        btn_ilerleme_kaydet = QPushButton("İlerleme Kaydet")
        btn_ilerleme_kaydet.clicked.connect(self.ilerleme_kaydet)
        layout_ilerleme_kaydet.addWidget(lbl_sporcu_ad3)
        layout_ilerleme_kaydet.addWidget(self.input_sporcu_ad3)
        layout_ilerleme_kaydet.addWidget(lbl_antrenman_ad2)
        layout_ilerleme_kaydet.addWidget(self.input_antrenman_ad2)
        layout_ilerleme_kaydet.addWidget(lbl_ilerleme)
        layout_ilerleme_kaydet.addWidget(self.input_ilerleme)
        layout_ilerleme_kaydet.addWidget(btn_ilerleme_kaydet)
        layout.addLayout(layout_ilerleme_kaydet)

        # Rapor Al
        layout_rapor_al = QHBoxLayout()
        lbl_sporcu_ad4 = QLabel("Sporcu Adı:")
        self.input_sporcu_ad4 = QLineEdit()
        btn_rapor_al = QPushButton("Rapor Al")
        btn_rapor_al.clicked.connect(self.rapor_al)
        layout_rapor_al.addWidget(lbl_sporcu_ad4)
        layout_rapor_al.addWidget(self.input_sporcu_ad4)
        layout_rapor_al.addWidget(btn_rapor_al)
        layout.addLayout(layout_rapor_al)

        # Oluşturulan Programı Görüntüle
        layout_program_goruntule = QHBoxLayout()
        lbl_sporcu_ad5 = QLabel("Sporcu Adı:")
        self.input_sporcu_ad5 = QLineEdit()
        btn_program_goruntule = QPushButton("Programı Görüntüle")
        btn_program_goruntule.clicked.connect(self.program_goruntule)
        layout_program_goruntule.addWidget(lbl_sporcu_ad5)
        layout_program_goruntule.addWidget(self.input_sporcu_ad5)
        layout_program_goruntule.addWidget(btn_program_goruntule)
        layout.addLayout(layout_program_goruntule)

        # Rapor Alanı
        self.rapor_alani = QTextEdit()
        layout.addWidget(self.rapor_alani)

        self.setLayout(layout)

    def sporcu_ekle(self):
        ad = self.input_sporcu_ad.text()
        dal = self.input_sporcu_dal.text()
        sporcu = Sporcu(ad, dal)
        self.takip.sporcu_ekle(sporcu)
        QMessageBox.information(self, "Bilgi", "Sporcu başarıyla eklendi.")

    def program_olustur(self):
        ad = self.input_sporcu_ad2.text()
        sporcu = self.takip.sporcu_bul(ad)
        if sporcu:
            antrenman_adı = self.input_antrenman_ad.text()
            detaylar = self.input_antrenman_detay.text()
            sporcu.program_olustur(antrenman_adı, detaylar)
            QMessageBox.information(self, "Bilgi", "Program başarıyla oluşturuldu.")
        else:
            QMessageBox.warning(self, "Uyarı", "Sporcu bulunamadı.")

    def ilerleme_kaydet(self):
        ad = self.input_sporcu_ad3.text()
        sporcu = self.takip.sporcu_bul(ad)
        if sporcu:
            antrenman_adı = self.input_antrenman_ad2.text()
            ilerleme = self.input_ilerleme.text()
            if sporcu.ilerleme_kaydet(antrenman_adı, ilerleme):
                QMessageBox.information(self, "Bilgi", "İlerleme başarıyla kaydedildi.")
            else:
                QMessageBox.warning(self, "Uyarı", "Antrenman bulunamadı.")
        else:
            QMessageBox.warning(self, "Uyarı", "Sporcu bulunamadı.")

    def rapor_al(self):
        ad = self.input_sporcu_ad4.text()
        sporcu = self.takip.sporcu_bul(ad)
        if sporcu:
            rapor = sporcu.rapor_al()
            self.rapor_alani.setText(rapor)
        else:
            QMessageBox.warning(self, "Uyarı", "Sporcu bulunamadı.")

    def program_goruntule(self):
        ad = self.input_sporcu_ad5.text()
        sporcu = self.takip.sporcu_bul(ad)
        if sporcu:
            program = ""
            for antrenman in sporcu.antrenmanlar:
                program += f"{antrenman['ad']}: {antrenman['detaylar']}\n"
            self.rapor_alani.setText(program)
        else:
            QMessageBox.warning(self, "Uyarı", "Sporcu bulunamadı.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Arayuz()
    window.setWindowTitle("Sporcu Takip Sistemi")
    window.show()
    sys.exit(app.exec_())





