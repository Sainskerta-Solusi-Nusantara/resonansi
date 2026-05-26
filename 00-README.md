# Resonansi — Master README
**Versi:** v1.0 (Realized)
**Tanggal:** 2026-05-26
**Status:** Demo-ready · Pre-MVP

> Dokumen ini adalah **titik masuk** untuk seluruh deliverable Resonansi. Mulai dari sini bila Anda baru bergabung.

---

## 1. Apa Itu Resonansi?

**Resonansi** adalah marketplace dua-sisi yang mempertemukan **Brand Advocate Terverifikasi** dengan **Campaign Owner** (rumah produksi film, tim kampanye politik, brand, NGO). Reframing strategis dari "buzzer marketplace" → **infrastruktur advocacy yang akuntabel** — dengan compliance Bawaslu/PKPU built-in dan Tier 4–5 community network sebagai unfair advantage.

Untuk istilah lengkap, baca [**05-glossary.md**](./05-glossary.md).

---

## 2. Struktur Deliverable

```
/Users/haimac/buzzer/
│
├── 00-README.md                       ← Anda di sini · master navigator
├── 01-analisis-sistem-benchmarking.md ← Strategi, market sizing, kompetitor
├── 02-analisis-wireframe.md           ← Sitemap, IA, halaman aktual & backlog
├── 03-analisis-ui-ux.md               ← UX principles, design tokens
├── 04-pitchdeck.md                    ← 16 slide investor deck (Markdown)
├── 05-glossary.md                     ← Kamus istilah & terminologi
│
├── wireframes.html                    ← Master HTML (legacy SPA, semua screen jadi satu)
│
└── site/                              ← Multi-page HTML site (production-quality)
    ├── _build.py                      ← Script generator dari wireframes.html
    ├── _unify_nav.py                  ← Script unifikasi nav menu
    ├── _wire_auth.py                  ← Script wiring Masuk/Daftar CTA
    ├── _inject_auth_drawer.py         ← Script inject AUTH grup di drawer
    ├── assets/
    │   ├── style.css                  ← Shared CSS (design system terkode)
    │   └── icons.svg                  ← Sprite ikon Lucide-style
    ├── *.html (15 halaman root)
    ├── client/ (11 halaman dashboard)
    └── advocate/ (6 halaman supply side)
```

**Cara membuka demo:** `open site/index.html` di macOS, atau double-click. Tidak butuh server. Floating button "Demo · 32 halaman" di pojok kanan bawah untuk loncat antar halaman.

---

## 3. Status Halaman (32 dari estimasi ~52)

### ✅ Sudah Dibangun

| Kelompok | Jumlah | Halaman |
|---|---|---|
| **Auth** | 2 | login.html · signup.html (role tab Client/Advocate) |
| **Marketing** | 8 | index, how-it-works-client, how-it-works-advocate, solutions, about, trust, faq, contact |
| **Vertikal Publik** | 4 | film, politik, browse, pricing |
| **Design System** | 1 | design-system (live showcase) |
| **Client Dashboard** | 11 | dashboard, brief (wizard), campaigns (list), shortlist, advocate-detail, approval, live-campaign, library, analytics, billing, settings |
| **Advocate** | 6 | onboarding (6-step mobile), mobile (home), profile, campaigns, inbox, verification |

Total **32 halaman** · semua terhubung via real `<a href>` (bukan SPA). Lihat [02-analisis-wireframe.md](./02-analisis-wireframe.md) untuk detail per halaman.

### 🚧 Backlog (Direkomendasikan untuk MVP-Ready)

**MUST-HAVE sebelum launch publik (~6 halaman):**
1. Forgot Password / Reset Password
2. Email Verification (after signup)
3. Brief Detail (read-only view)
4. Apply to Brief (advocate-side flow dengan pitch tarif)
5. 4 Empty State pattern (advocate baru, client baru, no results, etc.)
6. 404 / Error page

**HIGH-PRIORITY untuk pitch & SEO (~5 halaman):**
7. Studi Kasus Detail (per case)
8. Notification Center (real, bukan banner)
9. Dispute / Report Issue
10. Welcome / First-Time Tour
11. Blog/Insight Article Detail

**MEDIUM (~5 halaman):**
12. Career / Karir listing
13. Press Kit
14. Bawaslu Audit View (public-facing)
15. e-Bukti Potong PPh (advocate)
16. Client mobile experience (responsive audit)

**LOW (Phase 2):**
17. Admin tools (moderation queue, KYC review queue)
18. API Documentation page (developer-facing)
19. Status / Maintenance page

Total estimasi: **52 halaman** untuk full MVP.

---

## 4. Reading Order untuk Audiens Berbeda

### Untuk Investor (15 menit)
1. [04-pitchdeck.md](./04-pitchdeck.md) — full pitch
2. Buka `site/index.html` + `site/how-it-works-client.html` di browser
3. (Opsional) [01-analisis-sistem-benchmarking.md](./01-analisis-sistem-benchmarking.md) §1, §7, §10

### Untuk Calon Co-Founder / Engineer (1 jam)
1. 00-README.md (Anda di sini)
2. [01-analisis-sistem-benchmarking.md](./01-analisis-sistem-benchmarking.md) §4 (arsitektur)
3. [02-analisis-wireframe.md](./02-analisis-wireframe.md) (sitemap & backlog)
4. [03-analisis-ui-ux.md](./03-analisis-ui-ux.md) (design principles)
5. Browse `site/design-system.html`

### Untuk Calon Client Tier-1 / Demo (10 menit)
1. Buka `site/index.html`
2. Klik "Cara Kerja" → tunjukkan 4-step journey
3. Klik "Mulai Gratis" → tunjukkan signup
4. Klik "Masuk" → login → `client/dashboard.html` → walkthrough
5. (Opsional) `site/trust.html` untuk klien politik

### Untuk Compliance Officer / Regulator
1. [05-glossary.md](./05-glossary.md) §5 (Compliance & Trust)
2. Buka `site/trust.html` & `site/client/approval.html`
3. [01-analisis-sistem-benchmarking.md](./01-analisis-sistem-benchmarking.md) §8 (Risiko & Mitigasi)

---

## 5. Konsistensi & Brand Discipline

Aturan yang **NON-NEGOSIASI** di seluruh materi (publik & internal):

1. **Tidak ada kata "buzzer"** di material publik. Gunakan **"Brand Advocate"** atau **"Endorser Bersertifikat"**.
2. **Hindari jargon militer** (target, serang, operasi, amunisi). Gunakan bahasa marketing (audiens, narasi, kampanye).
3. **Bahasa setara dua sisi**: "advocate & client" — bukan "talent & client".
4. **Compliance signal di setiap material politik** (disclaimer, audit trail mention).
5. **Vertical accent color hanya untuk badge/ilustrasi** — bukan untuk CTA. Primary CTA tetap brand blue + amber accent.

Lihat [03-analisis-ui-ux.md](./03-analisis-ui-ux.md) §6 (Voice & Tone) dan [05-glossary.md](./05-glossary.md) §12 (Istilah yang HARUS Dihindari).

---

## 6. Roadmap Tinggi-Level

| Fase | Bulan | Milestone | Halaman yang Diperlukan |
|---|---|---|---|
| **Foundation** | 0–3 | MVP internal, tim inti | 32 (sudah) + 6 MUST-HAVE = 38 |
| **Vertical Film Launch** | 4–6 | 2 rumah produksi beta, 500 advocate | + 5 HIGH-PRIORITY = 43 |
| **Vertical Politik Launch** | 7–9 | Pilot Pilkada 2027, compliance Bawaslu | + Bawaslu Audit View = 44 |
| **Scale-Up** | 10–14 | 5K advocate, 30 client aktif, mobile app | + 4 MEDIUM = 48 |
| **Series A** | 15–18 | USD 5–8 jt, brand & NGO expansion | + 4 LOW = 52 |

Lihat [04-pitchdeck.md](./04-pitchdeck.md) §Slide 13 (Roadmap) dan [01-analisis-sistem-benchmarking.md](./01-analisis-sistem-benchmarking.md) §9.

---

## 7. Demo Quick-Start

```bash
# Buka homepage
open /Users/haimac/buzzer/site/index.html

# Atau langsung ke design system showcase
open /Users/haimac/buzzer/site/design-system.html

# Atau master legacy (semua screen jadi satu, untuk overview cepat)
open /Users/haimac/buzzer/wireframes.html
```

**Flow yang sudah end-to-end:**
- Homepage → Masuk → Login form → Dashboard
- Homepage → Mulai Gratis → Signup (pilih Client) → Dashboard
- Homepage → Mulai Gratis → Signup (pilih Advocate) → Onboarding 6-step
- Sidebar dashboard → Buat Brief / Kampanye / Library / Analytics / Billing / Settings

---

## 8. Catatan untuk Maintenance

- **Master file:** `wireframes.html` (single-file, semua screen). Update di sini bila ada perubahan struktural.
- **Regenerate site/:** `python3 site/_build.py` — meng-overwrite semua file di `site/`.
- **Setelah regenerate, jalankan utility scripts:**
  ```bash
  python3 site/_unify_nav.py          # Konsistensi nav menu
  python3 site/_wire_auth.py          # Wiring CTA Masuk/Daftar
  python3 site/_inject_auth_drawer.py # AUTH grup di drawer
  ```
- **Auth pages** (`login.html`, `signup.html`) ditulis manual, bukan dari `_build.py`. Update langsung di file mereka bila perlu.

---

**Pertanyaan? Mulai dari [05-glossary.md](./05-glossary.md) atau buka demo di browser.**
