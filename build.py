# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_engine"))
from sitegen import *

EMAIL = "ssabato111@gmail.com"
SITE = dict(
    name="Sposabella", domain="www.sposabella.co.kr",
    brand_main="SPOSABELLA", brand_sub="스포사벨라 · Since 1995",
    desc="스포사벨라 — 1995년부터 이어온 인터내셔널 브라이덜 브랜드. 웨딩드레스, 파티드레스, 연주복, 맞춤정장. 서울 서초 아크로비스타.",
    og="2649b2_05fe499776144d0fb7aadeecd679acff~mv2.jpeg",
    address="112-4, Acrovista Lobby, 1685-3 Seocho-dong, Seocho-gu, Seoul (서울 서초구 서초동 1685-3 아크로비스타 로비 112-4)",
    tel="(02) 511-6117", tel_raw="025116117", fax="(02) 515-6117", email=EMAIL,
    footer_extra='<p>Open: Tue – Sun 10:00 – 19:30</p>',
    legal="Sposabella",
    social=[("Instagram", "https://instagram.com/ssabato1", IG_SVG), ("Facebook", "https://www.facebook.com/sposabellagroup", FB_SVG)],
    favicon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#2b2626"/><text x="32" y="43" text-anchor="middle" font-family="Georgia,serif" font-size="30" fill="#c9a98c">S</text></svg>',
    nav=[
        ("index.html", "Home", []),
        ("about.html", "About us", [("about.html#story", "Our Story"), ("about.html#history", "History")]),
        ("wedding-dress.html", "Wedding Dress", [("wedding-dress.html#c2018fw", "2018 F/W"), ("wedding-dress.html#c2018ss", "2018 S/S"), ("wedding-dress.html#c2017fw", "2017 F/W"), ("wedding-dress.html#c2016", "2016"), ("wedding-dress.html#archive", "Archive 1995–2014")]),
        ("celebrity.html", "Celebrity", []),
        ("wedding-hall.html", "Wedding Hall", []),
        ("contact.html", "Contact", []),
    ],
)

THEME = """:root{
  --ink:#2b2626; --ink-soft:#6b6262; --line:#e9e1dc; --paper:#fffdfb; --cream:#f7f1ec;
  --gold:#c9a98c; --gold-deep:#a3785a; --sky:#daeef3;
  --serif:"Cormorant Garamond",Georgia,serif; --sans:"Noto Sans KR","Apple SD Gothic Neo",sans-serif;
  --wrap:1180px; --header-h:76px;
}
.site-footer{background:#2b2626}
"""

HERO = "2649b2_05fe499776144d0fb7aadeecd679acff~mv2.jpeg"
def col(ids, dims=None):
    return [(f"2649b2_{i}", "P") for i in ids]

C2018FW = ["147415e0a4324a1fa73643a5cce62d29~mv2_d_2574_3861_s_4_2.jpg","9768fae1b02343d7adb6d48cc30f9d0b~mv2_d_2574_3861_s_4_2.jpg","9432343ad9de4a008fb57241552b9069~mv2_d_2574_3861_s_4_2.jpg","9da65931a4034ed597720c4987b2815f~mv2_d_2574_3861_s_4_2.jpg","ee5ad0c9c2e34c59b6f1b1b661422b95~mv2_d_3744_5616_s_4_2.jpg","ddbc6cf71e2741809914ba14094afdc7~mv2_d_3595_5392_s_4_2.jpg","a05a0f78692947ad964ac50221ff598f~mv2_d_2574_3861_s_4_2.jpg","80544a2aeee044a9a499430d7b6499eb~mv2_d_3744_5616_s_4_2.jpg","0d7feeeadbd2456fb097a9a997f27ce5~mv2_d_3582_5544_s_4_2.jpg","d77975499bc74d629589ea105ccc37de~mv2_d_3744_5616_s_4_2.jpg","7533cf4a62534b80964dddc979bf012d~mv2_d_3744_5616_s_4_2.jpg","c152c50030414bf4bb4a391bf961e56c~mv2_d_3744_5616_s_4_2.jpg","1b36383094ab4c20b55d9495e6e3c483~mv2_d_3744_5616_s_4_2.jpg","03e790fc511d4dc3b8e720a88599522b~mv2_d_3595_5392_s_4_2.jpg","1f6b0a58c6ba45a0b4343acc227dedb5~mv2_d_3744_5616_s_4_2.jpg","483f01b4af124c2291c14f2d8ff44e5f~mv2_d_2574_3861_s_4_2.jpg"]
C2018SS = [("018bb944906c4cf3a66d0abaeb2f41bf~mv2_d_3495_4558_s_4_2.jpg","P"),("237cc450f1a34141b52856b00fca0971~mv2_d_5322_3470_s_4_2.jpg","L"),("9aad433c59f64d01844a2755e2bd0933~mv2_d_3429_5349_s_4_2.jpg","P"),("721829c2318a4ec9a47c0ccfe91c01c0~mv2_d_3456_4508_s_4_2.jpg","P"),("04fead8f7c8e43559123e2e5208c5236~mv2_d_3456_5184_s_4_2.jpg","P"),("8dde78cbf72e496ebc9755382b5c0446~mv2_d_3456_5184_s_4_2.jpg","P"),("b6e23e65473d400ab6711cf8bf5c9c29~mv2_d_3456_5184_s_4_2.jpg","P"),("3ce5a6004fbb41bf95b8181a83e3f53d~mv2_d_3456_5184_s_4_2.jpg","P"),("6f2b1586eaef46a090d87c32b4cc3b66~mv2_d_3456_5184_s_4_2.jpg","P"),("81d0ed4be07744b591e19118ed3d5b67~mv2_d_3456_5184_s_4_2.jpg","P"),("ad1051da56b14fa1b96591a34fe240ea~mv2_d_3456_5184_s_4_2.jpg","P"),("a8a3414942cc44019ceb7edb04283cc9~mv2_d_3456_5184_s_4_2.jpg","P"),("db84235151164d34ba5d22b265ae38ca~mv2_d_3456_5184_s_4_2.jpg","P"),("b1485247d9fa4db8b577e86f83a8468d~mv2_d_3456_5184_s_4_2.jpg","P"),("97fadd06d80242849e8cf4a247d54c42~mv2_d_3456_5184_s_4_2.jpg","P"),("e65177e228df41de97e59d9f67ff8705~mv2_d_3456_5184_s_4_2.jpg","P"),("4f3240e9a8eb425b8078e8606ac10b4f~mv2_d_3456_5184_s_4_2.jpg","P"),("206973a5ae784f17af54fe404a57117e~mv2_d_3771_4919_s_4_2.jpg","P"),("18f101ac8be6410784cd054b020c1d5d~mv2_d_3456_4508_s_4_2.jpg","P")]
C2017FW = ["cfaf925f2a3942cdb16f0d2625ce53cc~mv2_d_5304_8100_s_4_2.jpg","f15376aab5ed4b02bc629db6bf28a2a4~mv2_d_5304_7952_s_4_2.jpg","3481ccc7532b4ca1b277b67f6e665a50~mv2_d_6508_9758_s_4_2.jpg","287d184eb4fe4993b997b07d9d9ce555~mv2_d_5087_7626_s_4_2.jpg","c3df0df46425444bb86b25fca09f8d34~mv2_d_5304_7952_s_4_2.jpg"]
C2016 = [("c5327da1459e43cdb2d3c87d4fb467db~mv2_d_2536_3170_s_4_2.jpg","P"),("f38a27239d16407e827776e38fc3cdff~mv2_d_5433_3425_s_4_2.jpg","L"),("c208da1d12b041048bda6b2860d80d24~mv2_d_2717_3425_s_4_2.jpg","P"),("ed0e90f5d7dd4526a47bef2b94dd7393~mv2_d_2717_3425_s_4_2.jpg","P"),("c69d857974f54852ba61f9ebccdfdb38~mv2_d_2717_3425_s_4_2.jpg","P")]
C2014 = ["fbd4d7304a264580b527fa1fcfdf4bd2~mv2.jpg","958e98a6f21242378cc8abc69f595670~mv2.jpg","5b3151e244c840d3a6df626a954d1b8b~mv2.jpg","536b705cfd8b443d92be3628bd2e9708~mv2.jpg"]
C2011 = ["d78bc11c846f49fe8c709c0d808219a5~mv2_d_2400_3000_s_4_2.jpg","14d942189ef7462aa29912ae25e5f383~mv2_d_2400_3000_s_4_2.jpg","4913d7938bbe47d89738adef6b67e366~mv2_d_2912_4368_s_4_2.jpg","b7724d7874f046c79c6fa12f1f8e78f9~mv2_d_2912_4368_s_4_2.jpg","240c812a06cd483f9f6adfbbe5ec830f~mv2_d_2912_4368_s_4_2.jpg"]
C2009 = ["97c044a039124ba789fb4f8bdad0de70~mv2_d_1628_2036_s_2.jpg","7f2e3ee03e874ceda75a009a85615c80~mv2_d_1628_2036_s_2.jpg","7e324dcece454e71aaf438f5d392e7e8~mv2_d_1590_1998_s_2.jpg","85c6f19f49ef492db71314ec64f26292~mv2_d_1628_2036_s_2.jpg","4a256534ac954a038dc0fb71905ff732~mv2_d_1628_2036_s_2.jpg","52c502abd7824e16a16192adc2fec43f~mv2_d_1580_2020_s_2.jpg"]
C2007 = ["7ec5a94decdf4d0693fbabfab5b602e3~mv2_d_2912_4368_s_4_2.jpg","b8db16c2bbde45d79da844cdc479a08e~mv2_d_2912_4368_s_4_2.jpg","400d0a8563084bcf8602dd03b6ece912~mv2_d_2912_4368_s_4_2.jpg","1f8d757847a748e6a328fae27902ff03~mv2_d_2912_4368_s_4_2.jpg","12a566a0ad1b4b5086ed298645b51df3~mv2_d_2912_4368_s_4_2.jpg","21110c7d998e4f4288de8d08839254b9~mv2_d_2912_4368_s_4_2.jpg"]
C2006 = [("5556bf8f138b4bceaa3398cfb6b50ac3~mv2_d_2551_3507_s_4_2.jpg","P"),("70c1fee04abf45f79e6f54e7d1c20f7e~mv2_d_2544_3504_s_4_2.jpg","P"),("9828101659cb4e58be8920850e999aea~mv2_d_2048_2811_s_2.jpg","P"),("b99d2abb55f442be990f4a30e9a68f99~mv2_d_1275_1753_s_2.jpg","P"),("3d855648994a4ee7b1ada74f12845962~mv2_d_2048_2511_s_2.jpg","P"),("b1c1561ce9a14ee1b52cf251afe4e541~mv2_d_2811_2048_s_2.jpg","L")]
C2003 = [("2cc49699de724d1184871d1ae5bab69b~mv2.jpg","P"),("8da53efa7ecf4fd6a68e539f9c527207~mv2.jpg","P"),("233286c05f8a4d2588e4e6085a25a6d0~mv2.jpg","P"),("3cb45b92f7cb4d2aa076e8ad5c7edc9c~mv2.jpg","P"),("9d678f0a23fa4e7ab77973fd910fb55b~mv2_d_1270_1384_s_2.jpg","P"),("762dd806284d4c72bde7601da524507d~mv2.jpg","P")]
C1999 = ["8a21a5103f9e4280b62b4d855f52ffcc~mv2_d_1231_1699_s_2.jpg","8762f5adc46d4a75b921fa389146fbb9~mv2_d_1276_1754_s_2.jpg","05ba77833b834e3abd8d055b2eccf98c~mv2.jpg","b1a73a33f91c47c2b3bdebabcc511b71~mv2_d_1253_1736_s_2.jpg","693d458f9bba4cb890b4e4eaaff087b1~mv2_d_1267_1741_s_2.jpg","4822876075044b5da1b21a1537807f60~mv2_d_1249_1736_s_2.jpg"]
C1995 = ["00295cfc9f8e40f1b70a687822869023~mv2.jpg","2b31e267934641d096147da232f90baf~mv2.jpg","cfca51c7004f4161893a4d4b2c85650d~mv2_d_1678_2216_s_2.jpg","b9826e59af614baa84e16c9b7b9b3801~mv2_d_1510_2232_s_2.jpg","d454d37151d74c8c989c6d526723849b~mv2_d_1518_2239_s_2.jpg","0b38b5bca65c4add9472a1d4179eaffd~mv2_d_1276_1754_s_2.jpg"]
MAIN = ["c4d010cad06745ddb3d856d39c19d69c~mv2_d_3456_5184_s_4_2.jpg","673a744cb8fd4f07b0156293e3c4d8b3~mv2_d_3776_5391_s_4_2.jpg","7028248338824ccd87e45743f5ae8313~mv2_d_2646_3779_s_4_2.jpg","f069021f1b0246a89b19cad4129b8dab~mv2_d_2646_3778_s_4_2.jpg","7db96b5a44784493912d6a4156015ff0~mv2_d_3456_5184_s_4_2.jpg","17f97f644e1e4fb4a4cd07ae2b82537e~mv2_d_2543_3930_s_4_2.jpg","7894fbf5a36744589bf8ffcc0d61e990~mv2_d_2646_3778_s_4_2.jpg","42a516097e8840bcafde33e1793489e3~mv2_d_3740_5340_s_4_2.jpg","cc5d073ea3f84fd98e99bf3c6f1bdea4~mv2_d_2620_3816_s_4_2.jpg","5d965134c2284798a0269c0ceeb386e2~mv2_d_3776_5391_s_4_2.jpg"]
CELEB = ["4de446fd8bbf42a6b353e8c318e27521~mv2.jpg","db2f34e6b1f6411b9ddd71de98ccf362~mv2.jpg","883a6a7903e344b2b072b98442d54870~mv2.jpg","2ef56f5a92744d7dbe1b0d7caf7b9754~mv2.jpeg","ad621a4b78a64e8bae826a5e6f0334ed~mv2.jpg","7d1cc2803a054adaa58a262a1be88368~mv2.jpg","960a4342b51147b8ab06a4b02b0caf7d~mv2.jpg","da9a0c6935d4474dba6bddf567c34f8f~mv2.jpg","81b67d101e9343f8927852f22c639331~mv2.jpg","a49ec3a0d7e84af29a5cb0f146d43787~mv2.jpg","22b56393530c4c6aae39d58f0babe5b1~mv2.jpg","1fef903fbb2d436f9583cc6973595418~mv2.jpg","b67705c522e74eb0929cdb1f22fb84c9~mv2.jpg","49780f2ca91f4d5ea6fcf597556343e2~mv2.jpg","a966e391ad2a466ba6e45172b2d67517~mv2.jpg","eabb106351ac4ccbabd44a6054391658~mv2_d_1518_2239_s_2.jpg","24012a4f1b80464f9a563612439e459c~mv2.jpg"]
VENUE = [("dfe22c5b27364cee9a24571a1d7b33fc~mv2.jpg","L"),("0ded9f54bdd941e3b0aff0f722c7f6c5~mv2.jpg","L"),("dc09fa2843df4bdf9c67640d80228780~mv2_d_3264_2448_s_4_2.jpg","L"),("17b42c9e7c2943f290e55b4bf4127a6f~mv2_d_3264_2448_s_4_2.jpg","L"),("ed95cf1b9bd044d6bee3523d333a7439~mv2_d_3264_2448_s_4_2.jpg","L"),("7ed12a7fb48e435d9a594948072a5050~mv2.jpg","L"),("8402bc41767e47a9bf73803b9747b914~mv2_d_5520_3680_s_4_2.jpg","L"),("0b9442f9ccae40a194cc00b047ed5958~mv2_d_4032_3024_s_4_2.jpg","L"),("0f6e73de1c07423f94bcf47149c9a9dd~mv2.jpg","L"),("d411844ddbec4a0ea669b643a98d7b16~mv2_d_2845_1745_s_2.jpg","L")]

P = lambda ids: [(f"2649b2_{i}", "P") for i in ids]
M = lambda ids: [(f"2649b2_{i}", o) for i, o in ids]

home = f"""
<section class="hero" style="background-image:url('{wix(HERO, 1920, 1280)}')">
  <div class="hero-inner">
    <p class="eyebrow">Sposabella · Since 1995</p>
    <h1>Something Special</h1>
    <p class="lead">Discover the designer bridal collection from Sposabella — effortless, understated glamour with a true sense of timeless beauty.</p>
    <div class="hero-cta">
      <a class="btn btn-light" href="wedding-dress.html">Wedding Dress</a>
      <a class="btn btn-outline" href="contact.html">Book your visit</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-img"><img src="{wix('2649b2_48ec484849154d42a9bac509fbd69849~mv2.jpeg', 900, 1200)}" loading="lazy" alt="Sposabella bridal"></div>
    <div class="split-text">
      <p class="eyebrow">Philosophy · Professionally Qualified</p>
      <h2>Various Kinds of Designs</h2>
      <p>For more than 20 years, Sposabella has been one of Korea's most recognized wedding dress houses and an international bridal brand with clients around the world. Explore a variety of wedding dresses at the Sposabella atelier — it will make your ceremony something new and truly memorable.</p>
      <p>스포사벨라는 1995년 오픈하여 최고급 웨딩드레스 회사로 운영되고 있는 인터내셔널 브랜드입니다. 웨딩드레스 · 연주복 · 파티드레스 · 맞춤정장.</p>
      <a class="btn" href="about.html">About Sposabella</a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <p class="eyebrow center">Collection</p>
    <h2 class="center">Sposabella Bridal Collection</h2>
    {gallery(P(MAIN[:8]), "gallery cols-4")}
    <p class="center"><a class="btn" href="wedding-dress.html">View all collections</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow center">Our Services</p>
    <div class="service-list">
      <div><h3>Wedding Dress</h3><p>오트쿠튀르 웨딩드레스 · 연주복 · 파티드레스</p></div>
      <div><h3>Wedding Consulting</h3><p>예식 컨셉부터 당일 연출까지</p></div>
      <div><h3>Party &amp; Flower</h3><p>Anniversary Flower와 함께하는 파티 플라워</p></div>
      <div><h3>Gift</h3><p>플라워 바스켓 · 난 선물</p></div>
      <div><h3>Wedding Hall</h3><p>세빛섬 플로팅아일랜드 · 마리나파크</p></div>
      <div><h3>Catering</h3><p>국제연회 셰프의 웨딩 디너</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap center">
    <p class="eyebrow">Sposabella Group</p>
    <div class="group-row">
      <a href="https://www.floatingisland.co.kr" target="_blank" rel="noopener"><img src="{wix('2649b2_2eff6fa5986b465db12ced985adb7511~mv2.jpg', 400, 160)}" alt="Floating Island" loading="lazy"></a>
      <a href="https://www.anniversaryflower.co.kr" target="_blank" rel="noopener"><img src="{wix('2649b2_4de5252b554e48bc82de758ee00aa01a~mv2.jpg', 400, 160)}" alt="Anniversary Party Flower" loading="lazy"></a>
      <a href="https://www.marinapark.co.kr" target="_blank" rel="noopener"><img src="{wix('2649b2_a140c96b7c0344ee95e9ac2ca9809c12~mv2.jpg', 300, 300)}" alt="Gift" loading="lazy"></a>
    </div>
  </div>
</section>

{cta("Come and visit us", "We enjoy creating new concepts and designs for our clients. Tue – Sun 10:00 – 19:30", "Book your visit · 02 511 6117", "tel:025116117", ("E-mail", f"mailto:{EMAIL}"))}
"""

about = f"""
{page_hero('2649b2_fe9b8844b85c41b897f0ac8f0de23978~mv2.jpg', 'Sposabella', 'About us')}
<section class="section" id="story">
  <div class="wrap split">
    <div class="split-img"><img src="{wix('2649b2_1a208eb6c2bc4068afb5ee886ae52c80~mv2.jpg', 1000, 700)}" loading="lazy" alt=""></div>
    <div class="split-text">
      <p class="eyebrow">Our Story</p>
      <h2>Over 25 years of bridal couture</h2>
      <p>스포사벨라는 1995년 오픈하여 25년간 최고급 웨딩드레스 회사로 운영되고 있는 인터내셔널 브랜드입니다. 웨딩드레스, 연주복, 파티드레스, 맞춤정장을 디자인하고 제작합니다.</p>
      <p>Sposabella opened in 1995 and has grown into an international bridal house known for haute-couture wedding dresses. Every gown is designed and produced by Sposabella — "we enjoy creating new concepts and design for our clients."</p>
    </div>
  </div>
</section>
<section class="section alt" id="history">
  <div class="wrap narrow">
    <p class="eyebrow center">History</p>
    <h2 class="center">Stunning weddings with Sposabella Bridal Collection</h2>
    <ul class="timeline">
      <li><span>1995</span>스포사벨라 오픈 — 서울 서초</li>
      <li><span>1999 – 2003</span>초기 컬렉션 · 오트쿠튀르 웨딩드레스 라인 확립</li>
      <li><span>2006 – 2011</span>셀러브리티 웨딩 · 파티드레스 · 연주복 라인 확장</li>
      <li><span>2014 – 2016</span>Feminine · Simple Modern 컬렉션</li>
      <li><span>2017 – 2018</span>S/S · F/W 시즌 컬렉션 발표</li>
      <li><span>Today</span>세빛섬 플로팅아일랜드 · 마리나파크 · 애니버셔리 플라워와 함께하는 토털 웨딩</li>
    </ul>
  </div>
</section>
{cta("Let's work together", "Tel 82 02 511 6117 · ssabato111@gmail.com · sposabella@naver.com", "Contact", "contact.html")}
"""

def collection(anchor, title, note, items, cls="gallery cols-4"):
    n = f'<p class="center sub">{note}</p>' if note else ""
    return f'<section class="section collection" id="{anchor}"><div class="wrap"><p class="eyebrow center">Collection</p><h2 class="center">{title}</h2>{n}{gallery(items, cls)}</div></section>'

dress = f"""
{page_hero('2649b2_c4d010cad06745ddb3d856d39c19d69c~mv2_d_3456_5184_s_4_2.jpg', 'Sposabella', 'Wedding Dress', 'Create your dream — create your wedding', tall=True)}
<nav class="jump wrap"><a href="#c2018fw">2018 F/W</a><a href="#c2018ss">2018 S/S</a><a href="#c2017fw">2017 F/W</a><a href="#c2016">2016</a><a href="#c2014">2014</a><a href="#c2011">2011</a><a href="#archive">Archive 1995 – 2009</a></nav>
{collection("main", "Signature", "", P(MAIN))}
{collection("c2018fw", "2018 F/W Wedding Dress", "", P(C2018FW))}
{collection("c2018ss", "2018 S/S Wedding Dress", "", M(C2018SS))}
{collection("c2017fw", "2017 F/W Wedding Dress", "", P(C2017FW), "gallery cols-3")}
{collection("c2016", "2016 Wedding Dress", "", M(C2016), "gallery cols-3")}
{collection("c2014", "2014 — Feminine wedding collection", "Feminine wedding collection of Sposabella", P(C2014), "gallery cols-4")}
{collection("c2011", "2011 — Simple Modern", "Simple Modern wedding Dress", P(C2011), "gallery cols-3")}
<section class="section alt" id="archive"><div class="wrap"><p class="eyebrow center">Archive</p><h2 class="center">1995 – 2009</h2>
<h3 class="center yr">2009</h3>{gallery(P(C2009), "gallery cols-4")}
<h3 class="center yr">2007</h3>{gallery(P(C2007), "gallery cols-4")}
<h3 class="center yr">2006</h3>{gallery(M(C2006), "gallery cols-4")}
<h3 class="center yr">2003 ~</h3>{gallery(M(C2003), "gallery cols-4")}
<h3 class="center yr">1999 ~</h3>{gallery(P(C1999), "gallery cols-4")}
<h3 class="center yr">1995 ~</h3>{gallery(P(C1995), "gallery cols-4")}
</div></section>
{cta("Book a fitting", "Tue – Sun 10:00 – 19:30 · Acrovista, Seocho", "02 511 6117", "tel:025116117", ("E-mail", f"mailto:{EMAIL}"))}
"""

celeb = f"""
{page_hero('2649b2_4de446fd8bbf42a6b353e8c318e27521~mv2.jpg', 'Sposabella', 'Celebrity')}
<section class="section"><div class="wrap"><p class="center sub">스포사벨라와 함께한 셀러브리티 웨딩과 미디어 화보.</p>{gallery([(f"2649b2_{i}", "L") for i in CELEB], "gallery cols-3")}</div></section>
{cta("Create your wedding", "", "Contact", "contact.html")}
"""

hall = f"""
{page_hero('2649b2_8402bc41767e47a9bf73803b9747b914~mv2_d_5520_3680_s_4_2.jpg', 'Wedding Hall', 'Design your wedding', 'Garden wedding · Convention wedding')}
<section class="section"><div class="wrap">
  <div class="split">
    <div class="split-text"><p class="eyebrow">Garden Wedding</p><h2>마리나파크 가든 웨딩</h2><p>한강과 서리풀 공원을 배경으로 화이트 가제보 아래에서 진행되는 야외 가든 예식. 하루 두 커플만 진행하는 여유로운 예식.</p><a class="btn" href="https://www.marinapark.co.kr" target="_blank" rel="noopener">Marina Park</a></div>
    <div class="split-text"><p class="eyebrow">Convention Wedding</p><h2>세빛섬 플로팅아일랜드</h2><p>한강 위 세빛섬 컨벤션홀에서 진행되는 대규모 컨벤션 웨딩. 국제연회를 진행해 온 셰프의 디너와 함께합니다.</p><a class="btn" href="https://www.floatingisland.co.kr" target="_blank" rel="noopener">Floating Island</a></div>
  </div>
  {gallery(M(VENUE), "gallery cols-3")}
</div></section>
{cta("Wedding consulting", "드레스부터 예식장, 플라워, 케이터링까지 — 스포사벨라 그룹이 함께 준비합니다.", "Contact", "contact.html")}
"""

contact = f"""
{page_hero('2649b2_05fe499776144d0fb7aadeecd679acff~mv2.jpeg', 'Sposabella', 'Contact')}
<section class="section"><div class="wrap split contact-split">
  <div class="split-text">
    <h2>Come and visit us</h2>
    <p>We enjoy creating new concepts and designs for our clients. 방문 상담은 예약제로 진행됩니다.</p>
    <div class="contact-card">
      <h3>SPOSABELLA</h3>
      <p>112-4, Acrovista Lobby, 1685-3 Seocho-dong, Seocho-gu, Seoul<br>서울 서초구 서초동 1685-3 아크로비스타 로비 112-4</p>
      <p>Tel: <a href="tel:025116117">(02) 511-6117</a><br>Fax: (02) 515-6117</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="mailto:sposabella@naver.com">sposabella@naver.com</a></p>
      <p>Open: Tue – Sun 10:00 – 19:30 (Mon closed)</p>
      <p class="social-row"><a href="https://instagram.com/ssabato1" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.facebook.com/sposabellagroup" target="_blank" rel="noopener">Facebook</a></p>
    </div>
  </div>
  {contact_form(EMAIL, ["Wedding Dress 방문 상담", "Party Dress / 연주복", "맞춤정장", "Wedding Consulting", "기타 / Other"])}
</div></section>
<section class="map-section"><iframe title="Sposabella 위치" src="https://www.google.com/maps?q=%EC%84%9C%EC%9A%B8+%EC%84%9C%EC%B4%88%EA%B5%AC+%EC%84%9C%EC%B4%88%EB%8F%99+1685-3+%EC%95%84%ED%81%AC%EB%A1%9C%EB%B9%84%EC%8A%A4%ED%83%80&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe></section>
"""

PAGES = {
    "index.html": ("Home", home, True),
    "about.html": ("About us", about, False),
    "wedding-dress.html": ("Wedding Dress", dress, False),
    "celebrity.html": ("Celebrity", celeb, False),
    "wedding-hall.html": ("Wedding Hall", hall, False),
    "contact.html": ("Contact", contact, False),
}

EXTRA_CSS = """
.service-list{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-top:2.5rem;text-align:center}
.service-list h3{margin-bottom:.2em}.service-list p{color:var(--ink-soft);font-size:.9rem}
.group-row{display:flex;gap:2.5rem;justify-content:center;align-items:center;flex-wrap:wrap;margin-top:1.5rem}
.group-row img{height:70px;width:auto;object-fit:contain;filter:grayscale(1);opacity:.75;transition:.3s}.group-row a:hover img{filter:none;opacity:1}
.timeline{list-style:none;padding:0;margin:2rem 0 0;border-left:1px solid var(--gold)}
.timeline li{padding:.6rem 0 .6rem 1.5rem;position:relative;color:var(--ink-soft)}
.timeline li::before{content:"";position:absolute;left:-5px;top:1.2rem;width:9px;height:9px;border-radius:50%;background:var(--gold)}
.timeline span{display:block;font-family:var(--serif);font-size:1.3rem;color:var(--ink)}
.jump{display:flex;flex-wrap:wrap;gap:.4rem 1.6rem;justify-content:center;padding:1.5rem 24px 0;font-size:.78rem;letter-spacing:.18em;text-transform:uppercase}
.jump a{border-bottom:1px solid transparent;padding:.2rem 0}.jump a:hover{border-color:var(--gold)}
.collection{padding-top:3rem;padding-bottom:1.5rem}
.yr{margin-top:3rem;letter-spacing:.2em}
.gallery.cols-4{grid-template-columns:repeat(4,1fr);grid-auto-rows:300px}
.gallery.cols-4 .g-item.portrait{grid-row:span 1}
.gallery.cols-3 .g-item.portrait{grid-row:span 2}
@media (max-width:820px){.service-list{grid-template-columns:1fr 1fr}.gallery.cols-4{grid-template-columns:repeat(2,1fr);grid-auto-rows:260px}}
"""

if __name__ == "__main__":
    build(SITE, PAGES, os.path.dirname(os.path.abspath(__file__)), THEME + EXTRA_CSS)
