# Meteor Kaçışı

Pygame Zero ile yazılmış küçük bir uzay oyunu. Gemini sağa sola kaydır, yukarıdan düşen meteorlardan kaç, geçen her meteor için 1 puan kazan.

Bu proje iki amaçla geliştirildi:

- **Pygame Zero'yu keşfetmek:** az kodla çalışan bir oyunun nasıl kurulduğunu görmek.
- **Çocuklara temel yazılım kavramlarını öğretmek:** değişken, koşul, döngü ve fonksiyonu ekranda hemen sonucu görülen örneklerle anlatmak.

Oyunun tamamı tek dosyadır (`meteor_kacisi.py`) ve görsel ya da ses dosyası gerektirmez; gemi ve meteorlar basit şekillerle çizilir.

## Çalıştırma

Gerekenler: [uv](https://docs.astral.sh/uv/) (Python'u ve Pygame Zero'yu kendisi kurar).

```
uv sync
uv run meteor_kacisi.py
```

## Kontroller

| Tuş | Ne yapar |
| --- | --- |
| Sol / sağ ok | Gemiyi hareket ettirir |
| P | Oyunu durdurur, tekrar basınca devam ettirir |
| R | Oyunu baştan başlatır |

## Kodda neler var

| Kavram | Koddaki yeri | Ne anlatır |
| --- | --- | --- |
| Değişken | `skor`, `oyun_bitti`, `durdu` | Oyun bilgiyi nasıl aklında tutar |
| Koşul (`if`) | `update()` ve `on_key_down()` | "Eğer meteor gemiye çarptıysa oyun biter" gibi kurallar |
| Döngü (`for`) | `for meteor in meteorlar` | Aynı işi her meteor için tekrar etmek |
| Fonksiyon | `draw()`, `update()`, `yeniden_baslat()` | Bir işi adlandırıp tekrar tekrar kullanmak |

Pygame Zero `draw()` fonksiyonunu ekranı çizmek için, `update()` fonksiyonunu ise saniyede 60 kez oyunu ilerletmek için kendisi çağırır.

## Dene ve değiştir

Kodu öğrenmenin en iyi yolu onu değiştirmektir:

- Meteorları hızlandır: `meteor.y += 4` satırındaki 4'ü büyüt.
- Daha fazla meteor ekle: `range(3)` içindeki 3'ü değiştir.
- Geminin rengini değiştir: `"deepskyblue"` yerine `"limegreen"` yaz.
- Kenar kontrolünü sil: `and gemi.left > 0` kısmını kaldır ve geminin ekrandan çıkışını izle.
- Kendi kuralını yaz: skor 10 olunca meteorlar hızlansın.