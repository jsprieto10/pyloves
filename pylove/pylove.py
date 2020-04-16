"""Main module."""
from googletrans import Translator
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from random import randint

translator = Translator()


def password_to_key(password_provided):
    password = password_provided.encode() # Convert to type bytes
    salt = b'\xef\xfc\xb0\x00\x0b\xb5E\x95\xa8\xb8\x12\x9ch\xed&q'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend())
    return  base64.urlsafe_b64encode(kdf.derive(password))

def encrypt_file(password,path):

    with open(path, 'rb') as f:
        data = f.read()
    fernet = Fernet(password_to_key(password))
    encrypted = fernet.encrypt(data)

    with open(path+'.bejaranoEncrypt', 'wb') as f:
        f.write(encrypted)



def decrypt_file(password,path):

    with open(path, 'rb') as f:
        data = f.read()

    fernet = Fernet(password_to_key(password))
    encrypted = fernet.decrypt(data)
    with open('.'.join(path.split('.')[:-1]), 'wb') as f:
        f.write(encrypted)

def say_love():
    langs ="af,sq,am,ar,hy,az,eu,be,bn,bs,bg,ca,ceb,zh-CN,zh-TW,co,hr,cs,da,nl,en,eo,et,fi,fr,fy,gl,ka,de,el,gu,ht,ha,haw,he,hi,hmn,hu,is,ig,id,ga,it,ja,jv,kn,kk,km,ko,ku,ky,lo,la,lv,lt,lb,mk,mg,ms,ml,mt,mi,mr,mn,my,ne,no,ny,ps,fa,pl,pt,pa,ro,ru,sm,gd,sr,st,sn,sd,si,sk,sl,so,es,su,sw,sv,tl,tg,ta,te,th,tr,uk,ur,uz,vi,cy,xh,yi,yo,zu".split(',')
    dic={"af":"Afrikáans","sq":"Albanés","am":"Amárico","ar":"Árabe","hy":"Armenio","az":"Azerí","eu":"Vasco","be":"Bielorruso","bn":"Bengalí","bs":"Bosnio","bg":"Búlgaro","ca":"Catalán","ceb":"Cebuano","zh-CN":"Chino (simplificado)","zh-TW":"Chino (tradicional)","co":"Corso","hr":"Croata","cs":"Checo","da":"Danés","nl":"Holandés","en":"Inglés","eo":"Esperanto","et":"Estonio","fi":"Finlandés","fr":"Francés","fy":"Frisón","gl":"Gallego","ka":"Georgiano","de":"Alemán","el":"Griego","gu":"Guyaratí","ht":"Criollo haitiano","ha":"Hausa","haw":"Hawaiano","he":"Hebreo","hi":"Hindi","hmn":"Hmong","hu":"Húngaro","is":"Islandés","ig":"Igbo","id":"Indonesio","ga":"Irlandés","it":"Italiano","ja":"Japonés","jv":"Javanés","kn":"Canarés","kk":"Kazajo","km":"Jemer","ko":"Coreano","ku":"Kurdo","ky":"Kirguís","lo":"Laosiano","la":"Latín","lv":"Letón","lt":"Lituano","lb":"Luxemburgués","mk":"Macedonio","mg":"Malgache","ms":"Malayo","ml":"Malabar","mt":"Maltés","mi":"Maorí","mr":"Maratí","mn":"Mongol","my":"Birmano","ne":"Nepalí","no":"Noruego","ny":"Nyanja (Chichewa)","ps":"Pastún","fa":"Persa","pl":"Polaco","pt":"Portugués (Portugal y Brasil)","pa":"Panyabí","ro":"Rumano","ru":"Ruso","sm":"Samoano","gd":"Gaélico escocés","sr":"Serbio","st":"Sesoto","sn":"Shona","sd":"Sindhi","si":"Cingalés","sk":"Eslovaco","sl":"Esloveno","so":"Somalí","es":"Español","su":"Sundanés","sw":"Suajili","sv":"Sueco","tl":"Tagalo (filipino)","tg":"Tayiko","ta":"Tamil","te":"Telugu","th":"Tailandés","tr":"Turco","uk":"Ucraniano","ur":"Urdu","uz":"Uzbeko","vi":"Vietnamita","cy":"Galés","xh":"Xhosa","yi":"Yiddish","yo":"Yoruba","zu":"Zulú"}
    ix=randint(0, len(langs)-1)
    lang = langs[ix]
    text = "te amo con todo mi corazón"
    trans = translator.translate(text, dest=lang)
    print("lang:",dic[lang], "translation:" ,trans.text)
    return trans


if __name__ == '__main__':
    pass
