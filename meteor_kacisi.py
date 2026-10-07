import random
import pgzrun

WIDTH = 600
HEIGHT = 400
TITLE = "Meteor Kaçışı"

# Oyuncunun gemisi: (x, y, genişlik, yükseklik)
gemi = Rect(275, 350, 50, 30)

meteorlar = []
skor = 0
oyun_bitti = False
durdu = False


def yeniden_baslat():
    global skor, oyun_bitti, durdu

    # Gemi ortaya döner
    gemi.x = 275

    # Eski meteorlar silinir, yukarıya 3 yeni meteor konur
    meteorlar.clear()
    for i in range(3):
        meteorlar.append(Rect(random.randint(0, 560), -i * 150, 40, 40))

    skor = 0
    oyun_bitti = False
    durdu = False


def draw():
    screen.fill("midnightblue")
    screen.draw.filled_rect(gemi, "deepskyblue")
    for meteor in meteorlar:
        screen.draw.filled_circle(meteor.center, 20, "orange")
    screen.draw.text("Skor: " + str(skor), (10, 10), fontsize=30)
    screen.draw.text("P: Durdur   R: Yeniden başlat", topright=(590, 14), fontsize=20)

    if durdu:
        screen.draw.text("DURDURULDU", center=(300, 180), fontsize=60, color="yellow")
        screen.draw.text("Devam etmek için P tuşuna bas", center=(300, 235), fontsize=26)

    if oyun_bitti:
        screen.draw.text("OYUN BİTTİ", center=(300, 180), fontsize=60, color="red")
        screen.draw.text("Yeniden başlamak için R tuşuna bas", center=(300, 235), fontsize=26)


def update():
    global skor, oyun_bitti

    # Oyun bittiyse ya da durdurulduysa hiçbir şey hareket etmez
    if oyun_bitti or durdu:
        return

    # Sol ok tuşuna basılıyorsa gemi sola gider
    if keyboard.left and gemi.left > 0:
        gemi.x -= 5

    # Sağ ok tuşuna basılıyorsa gemi sağa gider
    if keyboard.right and gemi.right < WIDTH:
        gemi.x += 5

    for meteor in meteorlar:
        meteor.y += 4

        # Meteor ekranın altından çıktıysa: yukarı geri dönsün, 1 puan kazan
        if meteor.top > HEIGHT:
            meteor.y = -40
            meteor.x = random.randint(0, 560)
            skor += 1

        # Meteor gemiye çarptıysa: oyun biter
        if meteor.colliderect(gemi):
            oyun_bitti = True


def on_key_down(key):
    global durdu

    # R tuşuna basıldıysa oyun baştan başlar
    if key == keys.R:
        yeniden_baslat()

    # P tuşuna basıldıysa oyun durur, bir daha basılırsa devam eder
    if key == keys.P and not oyun_bitti:
        durdu = not durdu


yeniden_baslat()
pgzrun.go()