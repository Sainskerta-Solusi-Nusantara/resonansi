# Analisis UI/UX — Resonansi
**Versi:** v1.0 (Realized — design system live di `site/design-system.html`)
**Tanggal:** 2026-05-26
**Design Benchmark:** Tiket.com (discovery) + Sribu (friendly marketplace feel)
**Prinsip Inti:** Trust • Clarity • Speed

> **Bagian dari rangkaian dokumen Resonansi.** Mulai dari [00-README.md](./00-README.md) untuk overview.
>
> **Sumber kebenaran tunggal design system: `site/design-system.html`** — buka di browser untuk lihat live color palette, typography scale, button states, components, dan voice & tone. Dokumen ini berfungsi sebagai **prinsip & decision rationale**; spesifikasi visual yang konkret ada di showcase HTML.
>
> **Cross-reference:**
> - [00-README.md](./00-README.md) — overview project
> - [02-analisis-wireframe.md](./02-analisis-wireframe.md) — inventory halaman & komponen
> - [05-glossary.md](./05-glossary.md) — istilah (Brand Advocate, Tier, dll.)

---

## 1. Prinsip UX

### 1.1 Lima Pilar UX Resonansi
| Pilar | Apa Artinya di Produk | Manifestasi Visual |
|---|---|---|
| **Trust** | User percaya orang/transaksi di platform real & aman | Badge verified, foto KYC live, rating publik, escrow logo |
| **Clarity** | Tidak ada ambiguitas: apa yang dibayar, didapat, kapan | Pricing tertera di awal, status timeline visual, breakdown invoice |
| **Speed** | Brief → publish ≤ 12 menit, advocate apply ≤ 2 menit | Wizard pendek, smart defaults, autofill via AI |
| **Compliance** | Politik & sensitif tertangani aman | Watermark disclaimer, badge regulasi, audit trail accessible |
| **Dignity** | Advocate, terutama Tier 4–5, dihormati bukan dijadikan tool | Tone bahasa setara, kontrol penolakan brief, transparent rate-card |

### 1.2 Anti-Pattern yang Dihindari
- ❌ Dark pattern pricing (harga "mulai dari" yang menyesatkan)
- ❌ Bahasa militer/operasional ("target", "serang", "amunisi") untuk politik — gunakan bahasa marketing
- ❌ Auto-renew tersembunyi
- ❌ Skor publik yang merendahkan (jangan tampilkan "skor rendah" merah; gunakan "perlu ditingkatkan" netral)
- ❌ Modal/popup yang menghalangi fungsi inti

---

## 2. Design Tokens & Visual Foundations

### 2.1 Color Palette

**Primary — Trust Blue (turunan Tiket.com tapi diferensiasi sedikit lebih dalam)**
```
--brand-50  : #EAF3FF
--brand-100 : #CDE2FF
--brand-200 : #9AC4FF
--brand-300 : #5EA0FF
--brand-400 : #2E7DFB
--brand-500 : #0B5FE0   ← PRIMARY (warna identitas)
--brand-600 : #0A4FBB
--brand-700 : #093F94
--brand-800 : #082F6E
--brand-900 : #061F49
```

**Accent — Energy Amber (CTA & highlight, seperti Tiket "Tiketers")**
```
--accent-400 : #FFC83D
--accent-500 : #FFB400   ← CTA secondary, badge featured
--accent-600 : #E69E00
```

**Semantic**
```
--success : #16A34A
--warning : #F59E0B
--danger  : #DC2626
--info    : #2563EB
```

**Neutral**
```
--neutral-0   : #FFFFFF
--neutral-50  : #F8FAFC
--neutral-100 : #F1F5F9
--neutral-200 : #E2E8F0
--neutral-300 : #CBD5E1
--neutral-400 : #94A3B8
--neutral-500 : #64748B
--neutral-700 : #334155
--neutral-900 : #0F172A
```

**Vertical Accent (untuk diferensiasi context, dipakai sparing di badge/banner)**
```
Film     : #E11D48 (cinema red)
Politik  : #475569 (slate, sengaja netral & dewasa — bukan merah/biru partai)
Brand    : #7C3AED (purple energy)
NGO      : #059669 (mission green)
```

> **Catatan strategis:** Untuk vertical politik, **hindari merah/biru terang** yang asosiatif dengan partai tertentu. Pakai abu-abu slate untuk menegaskan netralitas platform.

### 2.2 Typography

**Font Family**
- **Display & Heading:** `Plus Jakarta Sans` (modern, Indonesia-friendly, mirip karakter Tiket.com)
- **Body:** `Inter` (legibility tinggi, multi-bahasa)
- **Monospace (data/code):** `JetBrains Mono`

**Type Scale (web)**
```
Display-XL : 56px / 64px / -1% / 700
Display-L  : 44px / 52px / -1% / 700
H1         : 32px / 40px /  0% / 700
H2         : 26px / 34px /  0% / 700
H3         : 20px / 28px /  0% / 600
H4         : 18px / 26px /  0% / 600
Body-L     : 16px / 24px /  0% / 400
Body       : 14px / 22px /  0% / 400
Caption    : 12px / 18px /  0% / 500
Tiny       : 11px / 16px /  0% / 500
```

**Type Scale (mobile)** — scale down 1 step, kecuali Body tetap 14–16.

### 2.3 Spacing (8-pt grid)
```
4 / 8 / 12 / 16 / 24 / 32 / 40 / 56 / 80 / 120
```

### 2.4 Radius
```
sm: 6px (input, badge)
md: 10px (button, card kecil)
lg: 16px (card utama)
xl: 24px (hero, modal)
full: 9999px (avatar, chip)
```

### 2.5 Elevation (Shadow)
```
sh-1 : 0 1px 2px rgba(15,23,42,0.06)        — card resting
sh-2 : 0 4px 12px rgba(15,23,42,0.08)       — card hover
sh-3 : 0 12px 32px rgba(15,23,42,0.12)      — modal, popover
sh-4 : 0 24px 56px rgba(15,23,42,0.16)      — hero / featured
```

### 2.6 Motion
```
ease-standard : cubic-bezier(0.2, 0, 0.2, 1)
duration-fast : 150ms
duration-base : 220ms
duration-slow : 360ms
```
- Hover lift card: 4px translateY + sh-2
- Page transition: fade + 8px slide
- Skeleton shimmer untuk loading

---

## 3. Component Library (Atomic)

### 3.1 Atoms
- **Button**: primary (brand-500 fill), secondary (outline brand-500), tertiary (ghost), danger, success. Size: sm/md/lg/xl. Loading state dengan spinner.
- **Input**: text, number, currency (auto Rp prefix), password, search (icon kiri), with error message slot
- **Badge**: verified, tier (Mega/Macro/Micro/Nano/Citizen), vertical (Film/Politik/Brand/NGO), status (Active/Pending/Done)
- **Avatar**: 24/32/40/56/80px, dengan status dot
- **Chip**: filter chip (removable), category chip
- **Icon set**: Lucide (konsisten, lightweight)

### 3.2 Molecules
- **Search Bar Vertical-Tabbed** — replica pola Tiket.com hero
- **Advocate Card** — foto, nama, niche, tier badge, reach, ER, rating, harga, CTA
- **Campaign Brief Card** — judul, vertical badge, deadline, budget range, match score, deliverables count
- **Price Block** — strikethrough discount, tier breakdown, "termasuk fee platform 14%"
- **Stat Tile** — angka besar + label + delta arrow (untuk dashboard)
- **Step Indicator** — wizard progress (horizontal di desktop, dot di mobile)

### 3.3 Organisms
- **Hero Section** dengan vertical tabs + search
- **Featured Carousel** (horizontal scroll cards)
- **Filter Sidebar** (desktop) / **Filter Bottom Sheet** (mobile)
- **Workflow Timeline** (Brief → Apply → Approve → Publish → Settle)
- **Comment Thread** (untuk content approval)
- **Analytics Dashboard Block** (chart + KPI tiles)

---

## 4. Pola Interaksi Kunci

### 4.1 Vertical Tabbed Search (signature pattern dari Tiket)
- 4 tabs: Film | Politik | Brand | NGO
- Setiap tab mengubah field filter di bawah (sama seperti Tiket "Pesawat" vs "Hotel" punya field berbeda)
- Default tab = Film (siklus singkat, easier sell pertama)

### 4.2 Match Score Display
- Tampilkan persentase (94%) + label kualitatif (Sangat Cocok / Cocok / Kurang Cocok)
- Tooltip menjelaskan: "Berdasarkan niche, lokasi, demografi audiens, dan riwayat performa"
- **Penting:** Skor di bawah 60% jangan ditampilkan merah — gunakan abu-abu + label "Eksploratif"

### 4.3 Approval Workflow — Side-by-Side
- Konten preview kiri, komentar/feedback kanan
- Tombol CTA: Tolak / Minta Revisi / Setujui — semua jelas, tidak ada destructive yang tersembunyi
- Setiap state perubahan masuk audit log otomatis (penting untuk politik)

### 4.4 Live Campaign Dashboard
- Refresh otomatis setiap 60 detik (debounced)
- KPI tiles dengan delta dari kemarin
- Alert system: anomaly detection (engagement drop, content flagged)
- Drilldown: klik tile → detail per konten / per advocate

### 4.5 Mobile-First untuk Advocate
- Bottom nav 5 ikon: Home / Peluang / Inbox / Earning / Profil
- Swipe gesture untuk: terima/tolak peluang (tipe Tinder, dengan konfirmasi)
- Push notif: peluang baru, tenggat aplikasi, pembayaran masuk

---

## 5. Accessibility & Inklusivitas

- WCAG 2.2 AA — kontras minimum 4.5:1 untuk teks normal, 3:1 untuk teks besar
- Keyboard navigation lengkap (Tab, Enter, Esc, arrow keys)
- Screen reader: semantic HTML, ARIA labels untuk komponen kompleks
- Reduced motion: hormati `prefers-reduced-motion`
- **Bahasa Indonesia primary, Inggris secondary, EN→ID toggle di header**
- Pertimbangan literacy rendah (penting untuk Tier 4–5):
  - Gunakan ikon + label, jangan ikon saja
  - Currency tertulis "Rp 1.200.000" bukan "1,2M" di flow transaksi
  - Voice-over instruksi onboarding (opsional)

---

## 6. Konten & Tone

### 6.1 Voice
- **Setara, profesional, hangat.** Bukan "klien & talent" — gunakan "Anda & advocate / advocate & klien" konsisten dua arah.
- **Hindari jargon militer/operasional.** Jangan: "target", "serangan narasi", "operasi". Pakai: "audiens", "narasi", "kampanye".
- **Hindari corporate-speak hampa.** Jangan: "synergize stakeholders". Pakai: "kerja sama dengan mitra".

### 6.2 Microcopy Examples
| Konteks | ❌ Buruk | ✓ Baik |
|---|---|---|
| Kosong (empty state) | "Tidak ada data" | "Belum ada peluang yang cocok. Coba longgarkan filter di atas." |
| Error | "Error 422" | "Profil belum lengkap. Tambahkan minimal 1 akun sosmed untuk lanjut." |
| Sukses | "Berhasil" | "Brief kamu sudah live. 247 advocate akan mendapat notifikasi." |
| Konfirmasi politik | "Setujui konten?" | "Setujui untuk publish. Konten akan otomatis menyertakan disclosure berbayar sesuai PKPU." |

---

## 7. Layout Patterns

### 7.1 Desktop Grid
- 12-column, max-width 1280px, gutter 24px
- Sidebar dashboard: 240px collapsed → 64px
- Content area minimum 720px

### 7.2 Mobile Grid
- 4-column, gutter 16px, edge padding 16px
- Sticky header 56px, bottom nav 64px
- Touch target minimum 44x44 px

### 7.3 Responsive Breakpoint
```
sm:  640px
md:  768px
lg:  1024px
xl:  1280px
2xl: 1536px
```

---

## 8. Komponen Khusus Vertikal Politik

### 8.1 Banner Compliance (selalu di atas brief politik)
```
┌─────────────────────────────────────────────────────────────┐
│ ⚠ Mode Kampanye Politik — Compliance Bawaslu Aktif          │
│ Disclosure, audit trail, dan filter SARA wajib aktif.        │
│ [Pelajari aturan]                                  [Setuju] │
└─────────────────────────────────────────────────────────────┘
```

### 8.2 Disclosure Auto-Append
- Setiap konten politik berbayar otomatis di-watermark: "Konten kampanye terverifikasi #Berbayar #PKPU"
- Tidak bisa dimatikan (hard rule untuk menjaga compliance moat)

### 8.3 Sentiment & Counter-Narrative Guardrail
- Sistem mendeteksi konten yang menyerang individu (bukan ide/program) → flagged untuk human review
- Filter hate-speech & SARA pakai model khusus Bahasa Indonesia (IndoBERT fine-tuned)

---

## 9. Onboarding — Detail UX

### 9.1 Advocate Onboarding (6 step, target 8 menit)
| Step | Cognitive Load | Hindari |
|---|---|---|
| 1. Welcome | rendah | Detail teknis di sini |
| 2. KYC | medium | Form panjang — pakai camera kit |
| 3. CV Upload | medium | Manual entry wajib — biarkan opsional, AI ekstrak |
| 4. Social Connect | medium | OAuth seharusnya 1 tap |
| 5. Preferensi | rendah | Pilihan terlalu banyak — limit 5–7 opsi |
| 6. Review | rendah | Surprise di sini — semua harus sudah jelas |

**Reward loop:** Setelah submit, tampilkan **estimasi penghasilan bulanan** berdasar profil — motivator kuat untuk completion.

### 9.2 Client Onboarding (3 step, target 5 menit)
1. Identitas perusahaan + NPWP (KYB)
2. Vertical primary (Film/Politik/Brand/NGO) + budget range bulanan
3. Verifikasi via email PIC → langsung ke "Create First Brief"

---

## 10. Empty States & Error Recovery

| State | Pesan + CTA |
|---|---|
| Advocate belum ada peluang | "Belum ada peluang yang cocok. Lengkapi profilmu untuk match yang lebih baik." [Lengkapi Profil] |
| Client belum ada brief | "Mulai brief pertamamu. Wizard kami akan memandu dalam 5 menit." [Buat Brief] |
| Tidak ada hasil filter | "Tidak ada advocate yang cocok. Coba longgarkan filter atau ubah niche." [Reset Filter] |
| Pembayaran gagal | "Pembayaran belum bisa diproses. Coba metode lain atau hubungi support." [Coba Lagi] [Hubungi CS] |
| Akun pending review | "Kami sedang verifikasi profilmu (rata-rata 24 jam). Notifikasi akan dikirim ke emailmu." [Tutup] |

---

## 11. Metrik UX (HEART Framework)

| Pilar | Metrik | Target Bulan 6 |
|---|---|---|
| **Happiness** | NPS Advocate, NPS Client | NPS ≥ 35 |
| **Engagement** | DAU/MAU Advocate, brief published per Client | DAU/MAU ≥ 25% |
| **Adoption** | Onboarding completion rate Advocate | ≥ 70% |
| **Retention** | M3 retention Client | ≥ 55% |
| **Task Success** | Brief published time, Match-to-hire conversion | ≤ 12 menit, ≥ 18% |

---

## 12. Design System Deliverables (Hand-off)

- [ ] Figma Library: Tokens, Atoms, Molecules, Organisms, Patterns
- [ ] Storybook (live components terkait stack frontend)
- [ ] Brand Guidelines PDF (1-pager untuk PR/marketing)
- [ ] Voice & Tone Doc
- [ ] Compliance Microcopy Library (terkurasi tim legal)
- [ ] Accessibility checklist per komponen

---

## 13. Kesimpulan UX Strategis

1. **Pola Tiket.com dipinjam, bukan disalin.** Vertical tab + search-first + trust strip = inti. Tapi diferensiasi via vertical accent color, palette lebih dalam (brand-500 lebih navy), dan typography lebih modern.
2. **Mobile-first untuk supply, desktop-first untuk demand.** Ini bukan "responsive nice-to-have" — ini perbedaan pola hidup user.
3. **Compliance bukan hambatan UX — itu fitur.** Audit trail dan disclosure otomatis adalah selling point untuk klien tier-1 yang risk-averse.
4. **Dignity layer untuk Tier 4–5.** Mereka adalah moat. UX yang merendahkan akan menggerus supply pool yang justru paling diferensiatif.
5. **Speed wins.** Tiap detik di brief wizard atau onboarding = drop-off. Investasi terbesar setelah MVP: AI autofill, smart defaults, prefill via integrasi.
