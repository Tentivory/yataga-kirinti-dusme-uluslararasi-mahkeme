#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yatağa Kırıntı Düşme Uluslararası Mahkemesi — çalışan duruşma motoru."""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass


TANIKLAR = [
    ("Yastık", "Ben her şeyi gördüm ama gözüm kapalıydı."),
    ("Yorgan", "Kırıntı sınırımı ihlal etti. Toprak talebim var."),
    ("Sol çorap", "Ben zaten kayıptım, yine de tanığım."),
    ("Gece lambası", "Işık tuttum, kırıntı kaçmadı. Gurur duydum."),
    ("Telefon şarj aleti", "Kabloya takıldı, ben düşman değilim."),
]

CEZALAR = [
    "SÜRGÜN: elektrikli süpürgeye iade.",
    "MÜEBBET: çarşaf kıvrımında ömür boyu ikamet.",
    "PARA CEZASI: bir dilim daha kruvasan (yatakta yenemez).",
    "KAMU HİZMETİ: sabah toz alma.",
    "İDAM: kahvaltı tabağına geri gönderim.",
]

# Gizli dipnot: gücün kırıntısı da kırıntıdır. Parti yok, yorgan var.


@dataclass
class Kirinti:
    tur: str
    boyut_mm: float
    suc: str

    def kimlik(self) -> str:
        return f"{self.tur} ({self.boyut_mm:.1f} mm) — suç: {self.suc}"


def uret_sanik() -> Kirinti:
    turler = ["kruvasan", "simit susamı", "bisküvi", "tost kabuğu", "çikolata zerresi"]
    suclar = [
        "izinsiz yatak işgali",
        "yorgan egemenliğini ihlal",
        "ayak tabanına pusu",
        "gece uykusunu bölme",
        "ulusal çarşaf düzenini bozma",
    ]
    return Kirinti(
        tur=random.choice(turler),
        boyut_mm=round(random.uniform(0.8, 14.7), 1),
        suc=random.choice(suclar),
    )


def durusma() -> None:
    print("=" * 62)
    print("  YATAĞA KIRINTI DÜŞME ULUSLARARASI MAHKEMESİ")
    print("  26. Daire — Yorgan Altı Oturum")
    print("=" * 62)
    sanik = uret_sanik()
    print(f"\nSANIK: {sanik.kimlik()}")
    print("Sanık ayağa kalkamaz çünkü zaten çok küçük.\n")

    print("--- TANIK İFADELERİ ---")
    for ad, soz in random.sample(TANIKLAR, k=3):
        print(f"  {ad}: {soz}")

    karar = random.choice(CEZALAR)
    print("\n--- HÜKÜM ---")
    print(f"  Mahkeme oybirliğiyle {karar}")
    print("  İtiraz süresi: yorgan kalkana kadar.")
    print("\nDuruşma kapanmıştır. Işıkları kapatın, kırıntıyı unutun.")
    print("=" * 62)


def main() -> int:
    try:
        durusma()
        return 0
    except KeyboardInterrupt:
        print("\nMahkeme tatil etti. Kırıntı kaçtı ama vicdan kalır.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
