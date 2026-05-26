# Analisis Sistem & Benchmarking
**Project Codename:** Resonansi (working title — alternatif: Amplify.id, Suara.co, Endorse.id)
**Kategori:** Two-Sided Marketplace untuk Brand Advocacy & Influence Marketing
**Vertikal Awal:** Film/Hiburan & Komunikasi Politik
**Tanggal:** 2026-05-26
**Disusun oleh:** Strategy Advisory
**Versi:** v1.0 — sinkron dengan deliverable lain

> **Bagian dari rangkaian dokumen Resonansi.** Mulai dari [00-README.md](./00-README.md) untuk overview.
>
> **Cross-reference:**
> - [02-analisis-wireframe.md](./02-analisis-wireframe.md) — Sitemap, inventory 32 halaman, backlog
> - [03-analisis-ui-ux.md](./03-analisis-ui-ux.md) — Design system principles
> - [04-pitchdeck.md](./04-pitchdeck.md) — Investor deck (16 slide)
> - [05-glossary.md](./05-glossary.md) — Kamus istilah (Advocate, Tier 1–5, take rate, dll.)
>
> Untuk istilah "Brand Advocate", "Tier 4–5", "Take rate", dll. — buka [05-glossary.md](./05-glossary.md).

---

## 1. Ringkasan Eksekutif

Resonansi adalah platform marketplace dua sisi yang mempertemukan **Brand Advocate** (individu dengan kapasitas memengaruhi audiens — KOL mikro, komunitas, mahasiswa, ibu rumah tangga digital, dll.) dengan **Campaign Owner** (rumah produksi film, distributor, tim kampanye politik, partai, lembaga survei, PR agency).

Reframing kata "buzzer" menjadi **"Brand Advocate"** atau **"Endorser Bersertifikat"** adalah keputusan strategis non-negosiasi. Konotasi "buzzer" di Indonesia sudah terdegradasi (asosiasi dengan akun anonim, disinformasi, troll). Platform yang ingin menarik klien tier-1 (Disney, Falcon, partai besar) harus memposisikan diri sebagai **"Influencer & Advocacy Marketplace"** yang verified, accountable, dan compliance-ready.

---

## 2. Analisis Pasar & Demand Sizing

### 2.1 Vertikal Film
| Kebutuhan Promosi | Window Waktu | Estimasi Spend per Judul |
|---|---|---|
| Pre-release awareness (teaser/trailer reaction) | T-30 s/d T-7 | Rp 200–800 juta |
| Premiere & special screening (penonton terkurasi) | T-7 s/d T-0 | Rp 100–500 juta |
| Opening weekend buzz (review, reels, twit) | T-0 s/d T+7 | Rp 300 juta–1.5 M |
| Sustain (mempertahankan layar bioskop) | T+7 s/d T+21 | Rp 100–400 juta |

**Pain point utama:** Layar bioskop turun dalam 7–14 hari jika okupansi rendah. Rumah produksi butuh **mobilisasi cepat** — saat ini lewat agency dengan markup 30–50% dan transparansi rendah.

### 2.2 Vertikal Politik
| Kebutuhan | Window | Estimasi Spend |
|---|---|---|
| Image building (long campaign) | 12–24 bulan | Rp 5–50 M / bulan |
| Issue response (war room) | < 24 jam | Rp 50–300 juta / isu |
| Mobilisasi massa offline (kampanye, kunjungan) | 1–3 bulan jelang pemilu | Rp 1–10 M / event |
| Konversi pemilih (door-to-door digital) | H-90 s/d H-1 | Rp 10–100 M |

**Pain point utama:** Kebutuhan **massa terverifikasi** (bukan bot) untuk bargaining power. Tim sukses saat ini mengelola ribuan kontak via spreadsheet & grup WA — tidak terukur, rentan fraud.

### 2.3 Total Addressable Market (TAM) Indonesia
- Influencer marketing Indonesia 2025: USD 220 juta (sumber: Statista) — tumbuh ~17% YoY
- Belanja kampanye politik nasional 2024: estimasi Rp 22 T (KPU + non-resmi)
- Belanja marketing film bioskop Indonesia: Rp 1.2–1.8 T/tahun
- **TAM blended: ~Rp 28 T/tahun** | **SAM (digital advocacy): ~Rp 6 T** | **SOM tahun 3: Rp 180 M (3% SAM)**

---

## 3. Benchmarking Kompetitor

### 3.1 Direct & Indirect Competitor
| Platform | Model | Kekuatan | Kelemahan vs Resonansi |
|---|---|---|---|
| **Sociabuzz (ID)** | Marketplace KOL self-service | Brand recognition, integrasi e-commerce | Tidak ada vertical politik; profiling dangkal |
| **Partipost (ID/SEA)** | Micro-influencer campaign | Skala besar, otomatisasi tinggi | Hanya transaksional, tidak ada advocacy jangka panjang |
| **Lemonilo Talent / Allstars** | Talent agency hybrid | Quality control, brand-safe | Manual, mahal, kurva supply terbatas |
| **Aspire.io (Global)** | End-to-end creator platform | UX excellent, analytics deep | Tidak fokus SEA, harga USD-based |
| **Grin (Global)** | Enterprise creator CRM | Workflow lengkap | Tidak ada layer "massa offline" |
| **NGOPI / Politicawave (ID)** | Political social listening | Data politik kuat | Tidak ada supply marketplace |

### 3.2 Design Benchmark — Tiket.com
Tiket.com dipilih sebagai north-star design karena:
1. **Trust signal kuat** — banner promo besar, badge verified, rating jelas
2. **Vertical-tab discovery** (Pesawat / Hotel / Kereta / Event) — pola yang akan kita adopsi (Film / Politik / Brand / NGO)
3. **Search-first homepage** dengan filter berlapis di hasil
4. **Card-based browsing** dengan harga + rating + jumlah review
5. **Color palette terpercaya** — biru navy (#0064D2) + putih + aksen kuning untuk CTA

**Elemen Tiket.com yang akan kita adaptasi:**
- Hero search bar dengan tab vertikal
- "Best Deals" carousel → "Featured Advocates" / "Trending Campaigns"
- Footer kepercayaan: payment partners, certifications, customer service
- Mobile-first dengan bottom-nav

---

## 4. Arsitektur Sistem (High-Level)

### 4.1 Modul Inti
1. **Identity & KYC Module**
   - KTP + selfie verification (Privy/Veriff)
   - Social account verification (Instagram, TikTok, X, YouTube OAuth)
   - Sertifikasi: badge "Verified Human", "Verified Reach", "Verified Politically-Neutral" / "Verified Affiliated"

2. **Supply Profiling Engine (CV Parser)**
   - Upload CV → NLP extraction (Education, Profession, Location, Languages, Demographics audience, Past engagement)
   - Auto-tagging: niche (parenting, gaming, food, politik-progresif, politik-konservatif, religi, dll.)
   - Skor: Authenticity (anti-bot), Reach, Engagement Rate, Sentiment History, Compliance Score

3. **Campaign Brief Module**
   - Wizard: tujuan (awareness / conversion / image / event-mobilization), target demografi, budget, timeline, deliverables, content guideline, do's & don'ts
   - Untuk politik: wajib field "afiliasi resmi", upload izin Bawaslu/KPU, disclaimer regulasi

4. **Matching & Recommendation**
   - Algoritma: similarity vector (advocate ↔ brief) + availability + budget fit + past performance + sentiment fit
   - Hybrid: algoritmik + human-curated untuk Tier-1 client

5. **Workflow & Content Approval**
   - Brief → Pitch → Approval → Content draft → Approval → Publish → Proof of work → Settlement
   - Versioning, comment thread, approval log (compliance trail untuk politik)

6. **Payments & Escrow**
   - Escrow (Midtrans/Xendit) — release saat proof-of-work terverifikasi
   - Tax withholding (PPh 21/23), invoice otomatis, e-Faktur ready
   - Multi-tier payout: per-task / retainer / performance bonus

7. **Analytics & Reporting**
   - Real-time dashboard: reach, engagement, sentiment, CPM, CPE
   - Untuk film: integrasi tracking link → bioskop (kerjasama XXI/CGV/Cinepolis)
   - Untuk politik: heat-map geografis, sentiment shift, share-of-voice

8. **Trust & Safety**
   - Bot detection (HypeAuditor-like)
   - Hate speech & SARA filter (mandatory di vertikal politik)
   - Dispute resolution + arbitrase

### 4.2 Stack Rekomendasi
- **Frontend:** Next.js 15 (App Router) + TypeScript + Tailwind + shadcn/ui
- **Backend:** NestJS atau Go (Fiber/Echo) — microservices untuk matching, payments, content
- **Database:** PostgreSQL (transactional) + ClickHouse (analytics) + Redis (cache, session)
- **Search/Match:** OpenSearch + vector DB (Pinecone/Qdrant) untuk semantic matching
- **CV Parsing:** Claude API (structured extraction) — hemat token via prompt caching
- **Storage:** S3-compatible (Cloudflare R2)
- **CDN/Edge:** Cloudflare
- **Observability:** OpenTelemetry + Grafana + Sentry

### 4.3 Diagram Konseptual (text)
```
[Advocate Mobile App] ─┐
                       ├─► [API Gateway] ─► [Auth] ─► [Identity/KYC]
[Client Web Dashboard] ┘                  ├─► [Profiling Engine] ◄── [LLM CV Parser]
                                          ├─► [Matching Service]  ◄── [Vector DB]
                                          ├─► [Campaign Workflow]
                                          ├─► [Content Approval]
                                          ├─► [Payments/Escrow]   ◄── [Midtrans/Xendit]
                                          └─► [Analytics]         ◄── [ClickHouse]
                                                                       ▲
                                                  [Social Listening] ──┘
```

---

## 5. Supply-Side Segmentation (Brand Advocate)

| Tier | Definisi | Reach | Use Case Dominan |
|---|---|---|---|
| **Tier 1 — Mega** | >1 juta follower verifikasi | Massive | Kampanye nasional, opening film besar |
| **Tier 2 — Macro** | 100K–1jt | Wide | Kampanye regional, sustain film |
| **Tier 3 — Micro** | 10K–100K | Niche | Targeted (parenting, mahasiswa, religi) |
| **Tier 4 — Nano / Community Lead** | <10K + komunitas offline | Hyper-local | Mobilisasi event, kampanye politik door-to-door, special screening |
| **Tier 5 — Citizen Advocate** | Tidak harus punya follower besar | Word-of-mouth | Polling, fokus grup, voter outreach |

Pendekatan **CV-based profiling** memungkinkan Tier 4–5 (yang biasanya tidak terjangkau platform influencer konvensional) menjadi diferensiator utama Resonansi — ini lah yang relevan untuk **bargaining power massa** di politik.

---

## 6. Demand-Side Segmentation (Campaign Owner)

| Segmen | Karakteristik | ARPU/tahun | Akuisisi |
|---|---|---|---|
| Rumah produksi film besar (Falcon, Visinema, MD) | 4–8 judul/tahun | Rp 800 jt–2 M | Sales enterprise, account manager |
| Distributor & jaringan bioskop | Co-marketing | Rp 200–600 jt | Partnership |
| Streaming platform (Vidio, Netflix lokal) | Original content launch | Rp 500 jt–1.5 M | Sales enterprise |
| Tim sukses politik (Pilpres/Pileg/Pilkada) | Musiman intens | Rp 2–20 M | Direct, partner konsultan politik |
| Partai politik (long-term image) | Retainer | Rp 500 jt–1 M/bulan | Direct |
| Kementerian/Lembaga (sosialisasi program) | Tender | Rp 300 jt–2 M/program | Tender + LKPP |
| Brand FMCG/Telco (cross-vertical upsell) | Continuous | Rp 100–500 jt | Self-service |

---

## 7. Revenue Model

1. **Take rate** 12–18% dari nilai transaksi (industri standar 10–20%)
2. **Subscription "Resonansi Pro"** untuk Campaign Owner: Rp 5–25 jt/bulan (akses analytics premium, account manager, priority matching)
3. **Verification fee** untuk Advocate: Rp 50–150 rb (one-time, untuk badge verified)
4. **Boost listing** Advocate: Rp 25–100 rb/minggu
5. **Data & insight subscription** untuk agency/lembaga survei: Rp 30–80 jt/bulan
6. **Managed service** (white-glove campaign management): retainer 20–30% dari budget

**Asumsi unit economics tahun 2:**
- GMV: Rp 120 M | Take rate blended: 14% | Revenue: Rp 16.8 M
- Gross margin: 65% | CAC payback: 9 bulan | LTV/CAC: 3.8x

---

## 8. Risiko & Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Stigma "buzzer" | Penolakan klien tier-1 | Rebrand total, content marketing edukasi, partnership PR agency |
| Regulasi Bawaslu (kampanye politik) | Sanksi, takedown | Compliance officer in-house, modul disclosure wajib, partnership lembaga audit |
| Akun bot / engagement palsu | Erosi trust | Multi-layer verification (KTP + biometrik + behavior analysis), public scoring |
| Konsentrasi musiman politik | Revenue dip non-pemilu | Diversifikasi: brand, NGO, lembaga, sosialisasi program pemerintah |
| Disinformasi & SARA | Reputasi platform | Content moderation AI + human, hate-speech filter, kill-switch kampanye |
| Persaingan Partipost/Sociabuzz | Squeeze pricing | Diferensiasi via vertikal politik & "Tier 4–5 community lead" yang tidak mereka punya |

---

## 9. Roadmap 18 Bulan

| Fase | Bulan | Milestone |
|---|---|---|
| **Foundation** | 0–3 | Tim inti, MVP web (Advocate signup + Client brief + matching manual), legal & compliance setup |
| **Vertical Film Launch** | 4–6 | Beta closed dengan 2 rumah produksi, 500 advocate verified, escrow live |
| **Vertical Politik Launch** | 7–9 | Pilot dengan 1 tim sukses Pilkada 2027, modul compliance Bawaslu |
| **Scale-Up** | 10–14 | 5,000 advocate, 30 client aktif, mobile app launch, analytics premium |
| **Series A & Expansion** | 15–18 | Buka Tier 4–5 community network, ekspansi vertical brand, Series A USD 5–8 jt |

---

## 10. Rekomendasi Strategis Eksekutif

1. **Jangan launch dengan nama "Buzzer".** Brand equity negatif terlalu mahal untuk diperbaiki.
2. **Mulai dari vertical Film** — siklus pendek, hasil cepat, reputasi cleaner → bangun trust → baru masuk politik.
3. **Bangun compliance moat lebih dulu.** Di Indonesia, regulasi politik akan semakin ketat. First-mover yang compliant menang.
4. **Tier 4–5 (community lead) adalah unfair advantage.** Inilah yang mengubah "buzzer marketplace" jadi "advocacy infrastructure".
5. **Tiket.com sebagai design benchmark = tepat** — vertical, trustworthy, mobile-native. Tapi pastikan UX untuk supply side (advocate) sesederhana Gojek mitra.
