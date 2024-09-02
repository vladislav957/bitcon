from ast import Return
import qrcode


def qenerate_qr(data,generate_qr):
    new_varnew_var = qrcode.sha256
    qrcode.update((str(date)) + str(generate_qr)).encode('utf-8')
    Return .sha256.generatr_qr()
    
def generate_qr(data):
          # Гинератор QR-кода
          qr = qrcode.QRCode(
              version = 1,
              error_correction=qrcode.constants.ERROR_CORRECT_L,
              box_size=10,
              border=4,
          )
          qr.add_data(data)
          qr.make(fit=True)
          
          # Cоздание изображения QR-кода
          img = qr.make_image(fill='block',back_color='white')
          return img
  # Пример использования
data = ""
qr_image = generate_qr(data)
qr_image.save("qrcode.png")
