# Analisis Wireframe & Halaman — Resonansi
**Versi:** v1.0 (Realized — sinkron dengan `/site/` multi-page)
**Tanggal:** 2026-05-26
**Status:** 32 halaman dibangun · 20 lagi di backlog

> **Catatan versi:** Versi v0.1 dokumen ini berisi wireframe ASCII low-fidelity sebagai eksplorasi awal. **Wireframe ASCII tersebut sudah di-superseded oleh halaman HTML production-quality di `/site/`.** Dokumen v1.0 ini sekarang berfungsi sebagai **inventory + IA spec + backlog roadmap**.
>
> Untuk overview keseluruhan project, baca [00-README.md](./00-README.md).
> Untuk istilah, baca [05-glossary.md](./05-glossary.md).

---

## 1. Sitemap & Information Architecture (Tingkat Atas)

```
Resonansi
│
├── Public (tidak perlu login)
│   ├── Marketing Surface
│   │   ├── Homepage
│   │   ├── How it Works (Client)        ← funnel B2B
│   │   ├── How it Works (Advocate)      ← funnel supply-side
│   │   ├── Solutions per Industri       ← vertical landing
│   │   ├── About / Tentang Resonansi
│   │   ├── Trust & Safety
│   │   ├── FAQ / Pusat Bantuan
│   │   └── Contact / Demo Request
│   │
│   ├── Vertical Pages (deep-dive per industri)
│   │   ├── Film (paket cepat + studi kasus)
│   │   ├── Politik (use case + compliance)
│   │   ├── Browse Advocates (discovery)
│   │   └── Pricing (3 tier)
│   │
│   ├── Design System Showcase           ← internal/portfolio
│   │
│   └── Auth
│       ├── Login                        ← split-screen design
│       └── Signup (role tab: Client/Advocate)
│
├── Client Dashboard (post-login, B2B)
│   ├── Home (overview kampanye)
│   ├── Buat Brief (Wizard 7-step)
│   ├── Kampanye (List dengan tabs Aktif/Draft/Selesai)
│   ├── Shortlist Advocate (per kampanye)
│   ├── Advocate Detail (single profile evaluation)
│   ├── Content Approval (workflow side-by-side)
│   ├── Live Campaign (real-time dashboard)
│   ├── Advocate Library (saved talents)
│   ├── Analytics (cross-campaign)
│   ├── Billing & Invoices
│   └── Settings (Profile, Notif, Team, Billing, API, Privacy)
│
└── Advocate (post-login, B2C)
    ├── Onboarding (6-step mobile, KYC + CV + Social)
    ├── Mobile App Home (peluang, earning, kampanye)
    ├── Profile Editor (public-facing profil)
    ├── My Campaigns (active, pending, past)
    ├── Inbox / Chat (per kampanye)
    └── Verification Center (badge progression)
```

---

## 2. Inventory Halaman Aktual (v1.0)

Total **32 halaman HTML** di `/site/`. Semua terhubung via real `<a href>` navigation.

### 2.1 Marketing & Public (15 halaman)

| Halaman | Path | Fungsi Utama | Catatan UX |
|---|---|---|---|
| Homepage | `site/index.html` | Hero search-first + vertical tabs + featured advocates + studi kasus + cara kerja + trust strip + mega footer | Tiket.com-inspired discovery |
| How it Works (Client) | `site/how-it-works-client.html` | 4-step journey + why-us + testimonial + CTA banner | Sribu-style step-by-step |
| How it Works (Advocate) | `site/how-it-works-advocate.html` | 4-step earning-focused + tier explanation + testimonial | Brand art berbeda (amber) |
| Solutions | `site/solutions.html` | 4 vertikal card (Film/Politik/Brand/NGO) + studi kasus carousel | Studi kasus masih teaser |
| About | `site/about.html` | Misi/visi + founding team + milestone timeline + advisor + investor | Team portraits gradient |
| Trust & Safety | `site/trust.html` | 5 pilar kepercayaan + dispute flow 4-step + sertifikasi (Bawaslu/Kominfo/ISO/PDP) | Critical untuk klien politik |
| FAQ | `site/faq.html` | Search hero + 4 category quick-link + accordion 10 Q&A + support CTA | Sribu-style accordion |
| Contact / Demo | `site/contact.html` | Form lead capture 2-column + sales pods per wilayah | Budget pre-selection chip |
| Film (vertical) | `site/film.html` | Paket cepat 3 tier (Premiere/Weekend/Sustain) + studi kasus okupansi + mitra bioskop | Aspek bisnis film-spesifik |
| Politik (vertical) | `site/politik.html` | Compliance banner + 6 use case + tier explanation + compliance card | Disclaimer Bawaslu wajib |
| Browse Advocates | `site/browse.html` | Sidebar filter + hasil card horizontal-row + pagination | Pola hotel listing Tiket |
| Pricing | `site/pricing.html` | 3 tier card (Self-Service/Pro/Enterprise) + FAQ tabs | Self-service vs enterprise |
| Login | `site/login.html` | Split-screen + SSO + email/password form | Submit → dashboard |
| Signup | `site/signup.html` | Split-screen + role tabs + dynamic art per role | Client → dashboard, Advocate → onboarding |
| Design System | `site/design-system.html` | Colors, typography, buttons, pills, forms, avatars, icons, spacing, voice & tone | Live source of truth |

### 2.2 Client Dashboard (11 halaman)

| Halaman | Path | Fungsi Utama | Pola UI |
|---|---|---|---|
| Dashboard Home | `site/client/dashboard.html` | KPI tile + alerts + tabel kampanye aktif + trend chart | Default landing post-login |
| Buat Brief | `site/client/brief.html` | Wizard 7-step (Tujuan → Vertikal → Audiens → Deliverables → Timeline → Guideline → Review) | Estimasi advocate match real-time |
| Kampanye (List) | `site/client/campaigns.html` | Tabs (Semua/Aktif/Draft/Selesai/Perlu Perhatian) + filter + table | Pagination + bulk action |
| Shortlist | `site/client/shortlist.html` | Filter sidebar + hasil advocate dengan match score 94%/91%/88% | Card horizontal-row dengan CTA |
| Advocate Detail | `site/client/advocate-detail.html` | Header profile + KPI stat + demografi audiens + sample konten + rate card | Untuk evaluasi tier-1 |
| Content Approval | `site/client/approval.html` | Preview konten kiri + komentar/audit trail kanan + 3 action button | Audit trail wajib untuk politik |
| Live Campaign | `site/client/live-campaign.html` | KPI live + chart reach harian + top content + alert anomaly | Auto-refresh 60 detik |
| Advocate Library | `site/client/library.html` | Tabs tag + bulk action + grid 4-col advocate | Saved talents per tag custom |
| Analytics | `site/client/analytics.html` | KPI cross-campaign + reach per vertikal (bar) + mix spend (donut) + top performer | Filter periode & vertikal |
| Billing & Invoices | `site/client/billing.html` | Saldo + escrow + spend + e-Faktur banner + table invoice | Compliance pajak ready |
| Settings | `site/client/settings.html` | Sub-nav kiri (Personal/Organisasi/Integrasi/Data) + content sections | Team table + integrasi card |

### 2.3 Advocate (6 halaman)

| Halaman | Path | Fungsi Utama | Catatan |
|---|---|---|---|
| Onboarding | `site/advocate/onboarding.html` | 6 step mobile (Welcome → KYC → CV → Social → Preferensi → Review) | Target 8 menit, ≥70% completion |
| Mobile App Home | `site/advocate/mobile.html` | Saldo + peluang + status kampanye + earning detail (3 phone mockup) | Bottom nav 5 ikon |
| Profile Editor | `site/advocate/profile.html` | Cover + avatar + about + niche + rate card + sambungan sosmed + badge | Public-facing preview |
| My Campaigns | `site/advocate/campaigns.html` | Tabs status + workflow timeline per kampanye | Revisi state highlighted |
| Inbox / Chat | `site/advocate/inbox.html` | List percakapan + chat thread side-by-side | Audit trail in-platform |
| Verification Center | `site/advocate/verification.html` | 5-step progression (Human → Reach → Brand Safe → Pro → Compliance) | Reward loop tier upgrade |

---

## 3. Backlog Halaman (Direkomendasikan Sebelum MVP-Launch)

Total estimasi: **20 halaman** lagi untuk full MVP-ready (~52 total).

### 3.1 MUST-HAVE (6 halaman) — sebelum launch publik

| # | Halaman | Rasional Bisnis | Estimasi |
|---|---|---|---|
| 1 | **Forgot Password** | Tanpa flow ini, password loss = churn permanent. Industri minimal. | 0.5 hari |
| 2 | **Reset Password** | Pasangan #1. Token verify lewat email. | 0.5 hari |
| 3 | **Email Verification** | Pasca-signup, sebelum bisa publish brief / apply. Compliance + anti-fake. | 0.5 hari |
| 4 | **Brief Detail (Read-Only)** | Setelah submit brief, client butuh halaman view kembali. Saat ini tidak ada — gap yang besar. | 1 hari |
| 5 | **Apply to Brief (Advocate)** | Sekarang advocate cuma "lihat detail" peluang. Tidak ada flow apply dengan pitch tarif. | 1 hari |
| 6 | **Empty States × 4** | Advocate baru (no opportunities) / Client baru (no campaigns) / No filter results / No notifications. UX cold-start. | 1 hari |
| 7 | **404 / Error Page** | Polish standar. | 0.25 hari |

### 3.2 HIGH-PRIORITY (5 halaman) — kuat untuk pitch & SEO

| # | Halaman | Rasional Bisnis | Estimasi |
|---|---|---|---|
| 8 | **Studi Kasus Detail** (1 template) | Saat ini cuma teaser di solutions.html. SEO + sales tier-1 sangat bergantung halaman ini. | 1.5 hari |
| 9 | **Notification Center** | Sekarang cuma banner inline. Real inbox notif untuk semua persona. | 1 hari |
| 10 | **Dispute / Report Issue** | Compliance moat butuh visible dispute flow public-facing. | 1 hari |
| 11 | **Welcome / First-Time Tour** | Setelah signup → tour 4-screen overlay. Onboarding completion booster. | 1 hari |
| 12 | **Blog / Insight Article (1 template)** | Untuk thought leadership + SEO + sales material. | 1.5 hari |

### 3.3 MEDIUM (5 halaman) — untuk skala & diferensiasi

| # | Halaman | Rasional Bisnis | Estimasi |
|---|---|---|---|
| 13 | **Career / Karir** | Talent acquisition signal. | 0.5 hari |
| 14 | **Press Kit / Media** | PR readiness. | 0.5 hari |
| 15 | **Bawaslu Audit View (Public)** | Diferensiator masif untuk klien politik tier-1. Lihat trail kampanye publik. | 2 hari |
| 16 | **e-Bukti Potong PPh (Advocate)** | Download view untuk advocate. Compliance fiskal. | 0.5 hari |
| 17 | **Client Mobile Experience Audit** | Saat ini Client desktop-only. Banyak Campaign Manager pakai mobile. | 2 hari (responsive) |

### 3.4 LOW (Phase 2 / Internal)

| # | Halaman | Catatan |
|---|---|---|
| 18 | Admin moderation queue | Bisa pakai Retool/internal tool, tidak perlu custom HTML |
| 19 | API Documentation (developer portal) | Untuk integration partner |
| 20 | Status / Maintenance page | Operational, simple |

---

## 4. Pola Interaksi & UX Kunci

### 4.1 Pola Lintas-Halaman yang Konsisten

| Pola | Lokasi | Catatan |
|---|---|---|
| **Web Header Nav** (6 item unified) | Semua marketing pages | Cara Kerja · Untuk Advocate · Solusi · Harga · Tentang · Kontak |
| **Sidebar Nav** | Client + Advocate dashboard | Real `<a>` link, active state per current page |
| **Mega Footer** | Semua marketing pages | 5-kolom: Brand + Produk + Solusi + Resources + Perusahaan |
| **Demo Drawer** (floating) | Semua 32 halaman | Cross-page navigation cepat untuk reviewer |
| **CTA Wiring** | Marketing pages | "Masuk" → login.html · "Mulai Gratis"/"Daftar" → signup.html |
| **Verification Pulse** (live-dot) | Live Campaign + Status pill | Animated CSS pulse hijau |

### 4.2 Pola UX yang Sebaiknya Ada di Backlog

| Pola | Diperlukan untuk | Status |
|---|---|---|
| **Approval Workflow Side-by-Side** | Content Approval | ✓ Ada |
| **Audit Trail visible** | Politik compliance | ✓ Ada |
| **Match Score Display** dengan tooltip | Shortlist + Advocate Detail | ✓ Ada (94/91/88 hardcoded) |
| **Wizard Step Indicator** | Brief Wizard, Onboarding | ✓ Ada |
| **Mobile-First untuk Advocate** | Onboarding + Mobile App | ✓ Ada |
| **Live Refresh** dengan auto-poll | Live Campaign | ✓ Visual hint (live-dot), bukan real polling |
| **Empty States** | Lihat backlog #6 | ❌ Belum ada |
| **Skeleton Loading** | Untuk halaman async | ❌ Belum ada (visual only) |
| **Tour / Walkthrough Overlay** | Lihat backlog #11 | ❌ Belum ada |

---

## 5. Information Architecture — Prinsip

1. **Vertical-first navigation** di public surface (mengikuti pola Tiket.com) — user langsung tahu "ini untuk apa".
2. **Search & discovery di atas hero** di homepage — sinyal bahwa platform adalah marketplace, bukan agency.
3. **Trust signal selalu visible** — badge, jumlah review, verified status muncul di setiap card.
4. **Compliance signal di vertical politik** — disclaimer, badge Bawaslu, audit trail accessible.
5. **Mobile-first untuk Advocate, Desktop-first untuk Client** — refleksi pola pemakaian: advocate akan pakai HP harian, client (PR/Agency) pakai laptop.
6. **Progressive disclosure di wizard** — 6–7 step pendek, bukan 1 form panjang.
7. **Audit trail accessible** — di setiap workflow yang sensitif (politik, dispute), tampilkan jejak aksi.
8. **Empty state dignified** — tidak menghakimi, kasih CTA actionable.

---

## 6. Halaman & Komponen yang Re-used

Daftar komponen yang dipakai berulang di beberapa halaman (sumber: `design-system.html` & `style.css`):

| Komponen | Dipakai di |
|---|---|
| `.web-header` + `.web-nav` | Semua 15 marketing pages |
| `.app-shell` + `.app-sidebar` | Semua 17 dashboard pages |
| `.card` (subtle) | Semua halaman |
| `.kpi` tile | Dashboard, Live Campaign, Analytics, Client Home, Advocate Profile |
| `.step-block` (4 variant warna) | How it Works × 2, Trust & Safety |
| `.feature-card` (5 variant) | How it Works, Solutions, Trust |
| `.testimonial` | How it Works × 2, Signup (split art) |
| `.cta-banner` | How it Works × 2 (end-of-page CTA) |
| `.mega-footer` | Semua 15 marketing pages |
| `.tab-row` | Browse, Library, Shortlist, Campaigns List, Live Campaign, Signup |
| `.wizard-steps` | Brief Wizard, Onboarding (visual) |
| `.v-stepper` | My Campaigns (advocate), Verification |
| `.data-table` | Billing, Campaigns List, Analytics, Dashboard, Settings (Team) |
| `.chat-thread` (chat-list + chat-pane) | Inbox |
| `.phone` (mockup frame) | Onboarding, Mobile App, Signup hero |
| `.match-ring` (conic gradient) | Shortlist, How it Works |

---

## 7. Checklist Validasi Sebelum Lanjut ke MVP

Sebelum coding production, validasi 9 hal ini dengan tim & user:

- [ ] **Tes 5-second** pada homepage: apakah user paham ini marketplace advocate?
- [ ] **Tes onboarding advocate** (KTP scan flow): completion rate ≥ 70% (acceptance threshold)
- [ ] **Tes brief wizard client**: completion rate ≥ 60%, time-to-publish ≤ 12 menit
- [ ] **Validasi compliance officer** untuk halaman `/politik` & `/client/approval`
- [ ] **Usability test Tier 4–5 advocate** (mungkin tech literacy lebih rendah) — pastikan onboarding bisa diselesaikan tanpa bantuan
- [ ] **Tes navigasi cross-page** di mobile (responsive sebagian belum di-audit)
- [ ] **Validasi konsistensi pill/badge** dengan brand guideline
- [ ] **Cek a11y (WCAG 2.2 AA)** kontras & keyboard nav
- [ ] **Walkthrough demo dengan 1 calon klien tier-1** sebagai test

---

## 8. Kesimpulan & Rekomendasi

1. **32 halaman sekarang sudah cukup untuk investor demo & sales pitch tier-1.** Brand reframe, design system, compliance positioning sudah terlihat jelas.
2. **6 MUST-HAVE halaman wajib dibangun sebelum launch publik** (estimasi ~5 hari kerja). Tanpa ini, ada friction yang menghentikan retention.
3. **5 HIGH-PRIORITY halaman wajib sebelum Series A** (~6 hari kerja). Tanpa Studi Kasus Detail, sales tier-1 lemah.
4. **MEDIUM/LOW** bisa pasca-Series A dengan tim engineering yang lebih besar.
5. **Audit halaman aktual:** beberapa pola yang absen di backlog (empty state, skeleton, tour) lebih impactful daripada menambah halaman baru. Prioritaskan pola UX dulu.

---

**Cross-reference:**
- [00-README.md](./00-README.md) — overview project
- [01-analisis-sistem-benchmarking.md](./01-analisis-sistem-benchmarking.md) — strategi & market
- [03-analisis-ui-ux.md](./03-analisis-ui-ux.md) — design system principles (sumber: `site/design-system.html`)
- [04-pitchdeck.md](./04-pitchdeck.md) — investor deck
- [05-glossary.md](./05-glossary.md) — istilah & terminologi
