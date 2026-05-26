"""Batch 2: case-study-detail, blog-detail, dispute, career, press"""
import sys
sys.path.insert(0, '/Users/haimac/buzzer/site')
from _build_new_pages import chrome, chrome_close, web_header, mega_footer, write_page


def page_case_study_detail():
    extra = '''<style>
    .cs-hero { position: relative; height: 520px; background: linear-gradient(180deg, rgba(6,15,40,0.2) 0%, rgba(6,15,40,0.85) 100%), url('https://images.unsplash.com/photo-1489599735188-7d76b3a1de7f?w=1600&q=80&auto=format&fit=crop') center/cover; color: #fff; display: flex; flex-direction: column; justify-content: flex-end; padding: 96px 40px 56px; }
    .cs-hero .container-narrow { max-width: 900px; margin: 0 auto; width: 100%; }
    .cs-hero h1 { font-size: 56px; line-height: 1.05; letter-spacing: -0.025em; color: #fff; margin: 14px 0 0; max-width: 800px; }
    .cs-meta { display: flex; gap: 18px; font-size: 13px; opacity: 0.85; margin-top: 18px; }
    .cs-meta span { display: inline-flex; align-items: center; gap: 6px; }
    .cs-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: -56px; position: relative; z-index: 5; padding: 0 40px; max-width: 900px; margin-left: auto; margin-right: auto; }
    .cs-stat { background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 32px 24px; box-shadow: 0 12px 36px rgba(15,30,60,0.12); text-align: center; }
    .cs-stat .num { font-family: var(--font-display); font-size: 44px; font-weight: 800; line-height: 1; letter-spacing: -0.025em; color: var(--accent); }
    .cs-stat .label { font-size: 13.5px; color: var(--muted); margin-top: 8px; }
    .cs-body { max-width: 760px; margin: 0 auto; padding: 80px 40px 0; }
    .cs-body h2 { font-family: var(--font-display); font-size: 32px; letter-spacing: -0.02em; margin: 56px 0 16px; }
    .cs-body p { font-size: 17px; line-height: 1.75; color: var(--grey-700); margin: 0 0 18px; }
    .cs-body p strong { color: var(--ink); }
    .cs-approach { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 32px; }
    .cs-approach-card { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 28px 24px; }
    .cs-approach-card .num { font-family: var(--font-display); font-size: 28px; font-weight: 800; color: var(--accent); margin-bottom: 8px; }
    .cs-approach-card h4 { margin: 0 0 6px; font-size: 16px; }
    .cs-execution { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 32px; }
    .cs-exec-card { border: 1px solid var(--line); border-radius: 14px; overflow: hidden; background: #fff; }
    .cs-exec-card img { width: 100%; height: 220px; object-fit: cover; display: block; }
    .cs-exec-card .body { padding: 22px; }
    .cs-results-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 24px; }
    .cs-result-block { background: linear-gradient(135deg, #0B5FE0 0%, #093F94 100%); color: #fff; border-radius: 14px; padding: 28px 20px; text-align: center; }
    .cs-result-block .num { font-family: var(--font-display); font-size: 36px; font-weight: 800; color: #FFB400; line-height: 1; }
    .cs-result-block .label { font-size: 12.5px; opacity: 0.85; margin-top: 8px; }
    .cs-quote { background: var(--accent-soft); border-left: 4px solid var(--accent); padding: 32px 32px; margin: 56px 0; border-radius: 0 12px 12px 0; }
    .cs-quote p { font-family: var(--font-display); font-size: 22px; line-height: 1.45; color: var(--ink); font-style: italic; margin: 0 0 16px; letter-spacing: -0.01em; }
    .cs-quote .author { display: flex; align-items: center; gap: 12px; }
    .cs-quote .author img { width: 48px; height: 48px; border-radius: 50%; object-fit: cover; }
    .cs-quote .author strong { font-size: 14px; }
    .cs-related { background: var(--grey-50); padding: 80px 40px; margin-top: 80px; }
    .cs-related .container-narrow { max-width: 1100px; margin: 0 auto; }
    .cs-related-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 32px; }
  </style>'''
    head = chrome('Film Drama A — 34% to 68% okupansi · Studi Kasus', '', 'case-study-detail.html', extra)
    body = f'''<section class="screen">
  <div class="frame">

    {web_header(active='')}

    <!-- Hero -->
    <div class="cs-hero">
      <div class="container-narrow">
        <div class="eyebrow" style="color: #FFB400; opacity: 1;">STUDI KASUS · FILM</div>
        <h1>Bagaimana Film Drama A naik dari 34% jadi 68% okupansi dalam 7 hari.</h1>
        <div class="cs-meta">
          <span>📅 Maret 2026</span>
          <span>⏱ 7 hari kampanye</span>
          <span>🎬 Falcon Pictures</span>
          <span>📍 12 kota</span>
        </div>
      </div>
    </div>

    <!-- At-a-glance stats -->
    <div class="cs-stats">
      <div class="cs-stat">
        <div class="num">34%</div>
        <div class="label">Okupansi awal<br>(H-1 sebelum kampanye)</div>
      </div>
      <div class="cs-stat" style="background: linear-gradient(135deg, #FFFAE6 0%, #fff 100%); border-color: #FFE08C;">
        <div class="num" style="color: #B58200;">68%</div>
        <div class="label">Okupansi akhir<br>(H+7 setelah kampanye)</div>
      </div>
      <div class="cs-stat">
        <div class="num">250</div>
        <div class="label">Advocate terlibat<br>(Tier 1–4 mix)</div>
      </div>
    </div>

    <div class="cs-body">

      <!-- The Challenge -->
      <h2>The Challenge</h2>
      <p>Film Drama A adalah produksi mid-budget dengan tema sosial yang kuat — tapi <strong>opening weekend-nya mengecewakan</strong>. Okupansi 34% dengan word-of-mouth lambat. Tim marketing Falcon Pictures khawatir film akan turun dari layar dalam 2 minggu, sebelum sempat menemukan audiensnya.</p>
      <p>Mereka butuh solusi yang bisa <strong>menggerakkan audiens organik</strong> — bukan paid media biasa. Audiens muda 18–28 di kota tier-1 dan tier-2 yang aktif di TikTok dan IG Reels. Kami diberi waktu 7 hari untuk membuktikan bisa membalikkan tren.</p>

      <!-- The Approach -->
      <h2>The Approach</h2>
      <p>Kami merancang kampanye "advocacy authentic" — bukan endorsement. Inti pendekatan: cari advocate yang <strong>secara natural relate</strong> dengan tema film, dan biarkan mereka bicara dengan suara mereka sendiri.</p>

      <div class="cs-approach">
        <div class="cs-approach-card">
          <div class="num">01</div>
          <h4>Smart Shortlisting</h4>
          <p class="small muted mb-0" style="line-height: 1.6;">AI matching engine memilih 1.200 advocate Tier 1–4 dari 12.500 pool, di-filter untuk niche cinephile, drama-lovers, dan komunitas mahasiswa.</p>
        </div>
        <div class="cs-approach-card">
          <div class="num">02</div>
          <h4>Pre-Launch Buzz</h4>
          <p class="small muted mb-0" style="line-height: 1.6;">50 Tier 1 advocate diberi akses early screening private di Jakarta dan Bandung. Konten reaksi mereka rilis 48 jam sebelum opening weekend.</p>
        </div>
        <div class="cs-approach-card">
          <div class="num">03</div>
          <h4>Opening Mobilization</h4>
          <p class="small muted mb-0" style="line-height: 1.6;">200 Tier 2–4 advocate posting reaction setelah nonton di hari pertama. Disclosure #KerjasamaResonansi otomatis dilampirkan untuk transparansi.</p>
        </div>
        <div class="cs-approach-card">
          <div class="num">04</div>
          <h4>Sentiment Monitoring</h4>
          <p class="small muted mb-0" style="line-height: 1.6;">Tim Falcon Pictures bisa lihat sentiment real-time. Saat ada negative spike di Yogya, kami re-allocate budget ke advocate Yogya untuk counter.</p>
        </div>
      </div>

      <!-- The Execution -->
      <h2>The Execution</h2>
      <p>Eksekusi dibagi dua phase. Phase 1: pre-launch (H-2 ke H-0). Phase 2: opening weekend (H+1 ke H+7). Total 250 advocate produced 580+ konten dalam 7 hari, mencapai 4.2 juta organic impression.</p>

      <div class="cs-execution">
        <div class="cs-exec-card">
          <img src="https://images.unsplash.com/photo-1505373877841-8d25f7d46678?w=1600&q=80&auto=format&fit=crop" alt="Pre-launch screening">
          <div class="body">
            <div class="eyebrow">PHASE 1</div>
            <h4 style="margin: 8px 0 6px;">Pre-Launch Buzz</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">50 advocate Tier 1 di-invite ke screening private. Reaction Reels mereka dilihat 1.2M dalam 48 jam — sebelum opening day.</p>
          </div>
        </div>
        <div class="cs-exec-card">
          <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=1600&q=80&auto=format&fit=crop" alt="Opening weekend">
          <div class="body">
            <div class="eyebrow">PHASE 2</div>
            <h4 style="margin: 8px 0 6px;">Opening Weekend Mobilization</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">200 advocate Tier 2–4 posting konten reaction setelah nonton. Pesan key: "film ini layak ditonton di bioskop, bukan streaming".</p>
          </div>
        </div>
      </div>

      <!-- Quote -->
      <div class="cs-quote">
        <p>"Resonansi tidak menjual endorsement — mereka memfasilitasi percakapan organik yang akan terjadi natural, dengan akuntabilitas. Untuk film yang butuh word-of-mouth, ini game-changer."</p>
        <div class="author">
          <img src="https://i.pravatar.cc/150?img=33" alt="Adi Sasongko">
          <div>
            <strong>Adi Sasongko</strong>
            <div class="small muted">Head of Marketing · Falcon Pictures</div>
          </div>
        </div>
      </div>

      <!-- Results -->
      <h2>Results</h2>
      <p>Dalam 7 hari, okupansi naik dari 34% jadi 68%. Tapi yang lebih penting: kampanye ini menghasilkan <strong>566K klik ke booking app</strong> (tiket.com, traveloka), dengan attribution yang bisa diukur. ROI 4.2x dari spend.</p>

      <div class="cs-results-grid">
        <div class="cs-result-block">
          <div class="num">+34pp</div>
          <div class="label">Okupansi increase<br>34% → 68%</div>
        </div>
        <div class="cs-result-block">
          <div class="num">4.2 M</div>
          <div class="label">Organic reach<br>across IG + TikTok</div>
        </div>
        <div class="cs-result-block">
          <div class="num">566K</div>
          <div class="label">Klik ke booking app<br>(measured attribution)</div>
        </div>
        <div class="cs-result-block">
          <div class="num">4.2x</div>
          <div class="label">ROI vs spend<br>(Rp 380 jt budget)</div>
        </div>
      </div>

      <h2>Pelajaran</h2>
      <p><strong>1. Advocate &gt; Endorser.</strong> Audiens muda Indonesia sudah cynic dengan endorsement. Tapi mereka percaya teman, mahasiswa, dan kreator niche yang punya audience real.</p>
      <p><strong>2. Disclosure justru menambah trust.</strong> Hashtag #KerjasamaResonansi yang transparent tidak menurunkan engagement — malah memperkuat persepsi profesional.</p>
      <p><strong>3. Burst &gt; Sustain untuk film.</strong> Film butuh peak mobilization di opening weekend. Resonansi memungkinkan kami compress 250 advocate ke 3-day window.</p>

    </div>

    <!-- Related case studies -->
    <div class="cs-related">
      <div class="container-narrow">
        <div class="eyebrow">RELATED STORIES</div>
        <h2 class="title" style="margin-top: 8px;">Lihat studi kasus lain.</h2>

        <div class="cs-related-grid">
          <a href="solutions.html" style="text-decoration: none; color: inherit;">
            <div class="card">
              <div style="aspect-ratio: 16/10; background: url('https://images.unsplash.com/photo-1591115765373-5207764f72e7?w=1600&q=80&auto=format&fit=crop') center/cover;"></div>
              <div class="card-body">
                <span class="pill politik">Politik</span>
                <h3 style="margin: 10px 0 6px; font-size: 17px;">Pilkada 2024: +12pp electability dalam 90 hari</h3>
                <p class="small muted mb-0">800 advocate mix, image building 6 bulan.</p>
              </div>
            </div>
          </a>
          <a href="solutions.html" style="text-decoration: none; color: inherit;">
            <div class="card">
              <div style="aspect-ratio: 16/10; background: url('https://images.unsplash.com/photo-1551434678-e076c223a692?w=1600&q=80&auto=format&fit=crop') center/cover;"></div>
              <div class="card-body">
                <span class="pill brand">Brand</span>
                <h3 style="margin: 10px 0 6px; font-size: 17px;">Mie Goyang: 4.2M reach, ER 6.8%</h3>
                <p class="small muted mb-0">320 micro & nano advocate, fokus mahasiswa.</p>
              </div>
            </div>
          </a>
          <a href="solutions.html" style="text-decoration: none; color: inherit;">
            <div class="card">
              <div style="aspect-ratio: 16/10; background: url('https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?w=1600&q=80&auto=format&fit=crop') center/cover;"></div>
              <div class="card-body">
                <span class="pill" style="background: var(--ngo); color: #0a6a3a; border-color: #a9d9bf;">NGO</span>
                <h3 style="margin: 10px 0 6px; font-size: 17px;">Kampanye Vaksin: awareness +47%</h3>
                <p class="small muted mb-0">Kolaborasi dengan Kementerian Kesehatan.</p>
              </div>
            </div>
          </a>
        </div>
      </div>
    </div>

    {mega_footer()}
  </div>
</section>'''
    return head + body + chrome_close()


def page_blog_detail():
    extra = '''<style>
    .blog-hero { padding: 80px 40px 40px; max-width: 900px; margin: 0 auto; }
    .blog-hero .eyebrow { margin-bottom: 16px; }
    .blog-hero h1 { font-size: 48px; line-height: 1.1; letter-spacing: -0.025em; margin: 0 0 24px; }
    .blog-meta { display: flex; align-items: center; gap: 16px; margin-bottom: 32px; }
    .blog-meta img { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; }
    .blog-meta strong { font-size: 14px; }
    .blog-meta .small { font-size: 12.5px; color: var(--muted); }
    .blog-featured { width: 100%; max-height: 480px; object-fit: cover; }
    .blog-body { max-width: 720px; margin: 0 auto; padding: 48px 40px 80px; }
    .blog-body h2 { font-family: var(--font-display); font-size: 28px; letter-spacing: -0.02em; margin: 48px 0 16px; }
    .blog-body p { font-size: 17px; line-height: 1.75; color: var(--grey-700); margin: 0 0 18px; }
    .blog-body p:first-of-type { font-size: 19px; color: var(--ink); }
    .blog-body p strong { color: var(--ink); }
    .blog-inline-img { width: 100%; border-radius: 12px; margin: 32px 0; }
    .blog-author-card { background: var(--grey-50); border: 1px solid var(--line); border-radius: 14px; padding: 24px; margin: 56px 0 0; display: flex; gap: 16px; align-items: flex-start; }
    .blog-author-card img { width: 64px; height: 64px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
    .blog-author-card h4 { margin: 0 0 4px; font-size: 16px; }
    .blog-related { background: var(--grey-50); padding: 64px 40px; }
    .blog-related .container-narrow { max-width: 1100px; margin: 0 auto; }
    .blog-related-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 32px; }
  </style>'''
    head = chrome('5 Pelajaran Reframing Buzzer ke Advocacy — Resonansi Blog', '', 'blog-detail.html', extra)
    body = f'''<section class="screen">
  <div class="frame">

    {web_header(active='')}

    <!-- Article hero -->
    <div class="blog-hero">
      <div class="eyebrow">PERSPECTIVE · INDUSTRI</div>
      <h1>5 Pelajaran Reframing "Buzzer" Menjadi Advocacy yang Akuntabel</h1>

      <div class="blog-meta">
        <img src="https://i.pravatar.cc/150?img=47" alt="Sari Wijaya">
        <div>
          <strong>Sari Wijaya</strong>
          <div class="small">Co-Founder & CTO Resonansi · 24 Apr 2026 · 8 menit baca</div>
        </div>
      </div>
    </div>

    <img class="blog-featured" src="https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=1600&q=80&auto=format&fit=crop" alt="Team discussion">

    <div class="blog-body">
      <p>Kata "buzzer" di Indonesia punya bobot negatif yang berat. Identik dengan akun anonim, spam, disinformasi politik, dan buy-engagement. Padahal — secara teknis — buzzer hanyalah <strong>orang yang menyuarakan pesan secara terorganisir</strong>. Apa yang membuatnya jadi pejorative bukan aktivitasnya, tapi <em>cara</em> aktivitas itu dilakukan.</p>

      <p>Sebagai tim yang membangun platform untuk industri ini, kami tahu kami tidak bisa lari dari word association ini. Kami harus <strong>membangun ulang konsepnya</strong>. Berikut 5 pelajaran yang kami dapat selama 2 tahun pertama.</p>

      <h2>1. Trust dimulai dari transparansi yang terlihat</h2>
      <p>Pelajaran pertama: trust tidak bisa di-claim. Trust harus bisa <strong>diverifikasi siapa saja</strong>. Itulah kenapa kami invest besar di audit trail publik untuk kampanye politik berbayar. Setiap aksi — siapa post apa, kapan, dibayar berapa — tercatat di immutable log yang bisa dibuka publik.</p>
      <p>Hasilnya counterintuitive: klien yang awalnya khawatir "terlalu transparan", justru jadi pendukung paling vokal. Karena disclosure membuat kampanye mereka punya <strong>credibility premium</strong> dibanding kompetitor opaque.</p>

      <img class="blog-inline-img" src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1600&q=80&auto=format&fit=crop" alt="Signing document">

      <h2>2. Tier ekonomi advocate butuh skala yang berbeda</h2>
      <p>Awalnya kami pikir matching engine yang baik cukup. Ternyata, tier ekonomi advocate (tier 1 = jutaan follower, tier 5 = community lead 50 follower) butuh <strong>workflow yang berbeda</strong>. Tier 1 mau email + meeting. Tier 5 mau WhatsApp dan pembayaran cepat ke e-wallet.</p>
      <p>Kami rebuild aplikasi mobile-first specifically untuk Tier 4–5, dengan onboarding 3-langkah dan KYC selfie. Hasilnya: <strong>tier 5 supply naik 8x</strong> dalam 6 bulan.</p>

      <h2>3. Compliance bukan checkbox — itu produk</h2>
      <p>Untuk vertikal politik, kami sadar awal bahwa compliance Bawaslu bukan sekadar "fitur tambahan". Itu <strong>core value proposition</strong>. Jika klien tim sukses bisa lapor LADK otomatis dengan satu klik, mereka tidak akan pindah platform.</p>
      <p>Jadi kami build modul khusus compliance: real-name disclosure, regional spending tracking, anti-coordination detection, dan automated reporting ke Sekretariat Bawaslu. Ini <strong>diferensiator yang tidak bisa di-replicate</strong> dengan cepat.</p>

      <img class="blog-inline-img" src="https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=1600&q=80&auto=format&fit=crop" alt="Indonesian street">

      <h2>4. Reputation matters — bahkan lebih dari fee</h2>
      <p>Pelajaran besar: advocate yang Tier 1–2 sering <strong>menolak kampanye yang fee-nya bagus</strong> jika mereka anggap kampanye itu menurunkan reputasi mereka. Kami tidak bisa lawan ini — kami harus <strong>memfasilitasinya</strong>.</p>
      <p>Solusi: setiap advocate punya "Reputation Score" yang naik kalau konten mereka authentic dan dapet engagement positif, dan turun kalau pernah terlibat dispute. Score ini visible ke advocate sendiri dan ke klien — menciptakan <strong>insentif kuat untuk quality over quantity</strong>.</p>

      <h2>5. Industry buruk bukan alasan kabur — tapi alasan masuk</h2>
      <p>Banyak founder yang skip industry ini karena "kotor". Kami percaya justru sebaliknya: <strong>justru karena kotor, kebutuhan akan platform akuntabel jauh lebih besar</strong>. Klien tier-1 sudah lelah dengan agency lama yang opaque. Advocate Tier 4–5 sudah lelah dibayar telat dan tidak transparent.</p>
      <p>Kami percaya kategori ini akan punya "platform yang bertanggung jawab" — sama seperti gojek menertibkan ojek tradisional, Tokopedia menertibkan e-commerce informal. Pertanyaannya hanya: <strong>siapa yang akan jadi platform itu</strong>.</p>

      <p style="margin-top: 48px; padding-top: 32px; border-top: 1px solid var(--line); font-style: italic; color: var(--muted);">
        Pendapat ini adalah pandangan penulis dan tidak harus mencerminkan posisi resmi PT Resonansi Suara Indonesia.
      </p>

      <!-- Author bio card -->
      <div class="blog-author-card">
        <img src="https://i.pravatar.cc/150?img=47" alt="Sari Wijaya">
        <div>
          <h4>Tentang Penulis — Sari Wijaya</h4>
          <p class="small muted mb-0" style="line-height: 1.7;">
            Co-Founder & CTO Resonansi. Sebelumnya 10 tahun engineering di Gojek dan ride-hailing. Bertanggung jawab atas matching engine, trust system, dan compliance Bawaslu modul.
          </p>
          <div class="row-tight" style="margin-top: 10px;">
            <a class="btn ghost small" style="padding-left: 0;" href="#">LinkedIn</a>
            <a class="btn ghost small" style="padding-left: 0;" href="#">X / Twitter</a>
            <a class="btn ghost small" style="padding-left: 0;" href="about.html">Tim →</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Related articles -->
    <div class="blog-related">
      <div class="container-narrow">
        <div class="eyebrow">ARTIKEL LAIN</div>
        <h2 class="title" style="margin-top: 8px;">Bacaan terkait.</h2>

        <div class="blog-related-grid">
          <a href="blog-detail.html" style="text-decoration: none; color: inherit;">
            <div class="card">
              <div style="aspect-ratio: 16/10; background: url('https://images.unsplash.com/photo-1497366216548-37526070297c?w=1600&q=80&auto=format&fit=crop') center/cover;"></div>
              <div class="card-body">
                <div class="eyebrow">BUILDING</div>
                <h3 style="margin: 10px 0 6px; font-size: 16px;">Cara kami merancang matching engine untuk 12.500 advocate</h3>
                <p class="small muted mb-0">6 menit baca · Bayu Hidayat</p>
              </div>
            </div>
          </a>
          <a href="blog-detail.html" style="text-decoration: none; color: inherit;">
            <div class="card">
              <div style="aspect-ratio: 16/10; background: url('https://images.unsplash.com/photo-1555899434-94d1368aa7af?w=1600&q=80&auto=format&fit=crop') center/cover;"></div>
              <div class="card-body">
                <div class="eyebrow">COMPLIANCE</div>
                <h3 style="margin: 10px 0 6px; font-size: 16px;">PKPU & Bawaslu Ready: 9 fitur compliance yang wajib ada</h3>
                <p class="small muted mb-0">10 menit baca · Maya Putri, SH</p>
              </div>
            </div>
          </a>
          <a href="blog-detail.html" style="text-decoration: none; color: inherit;">
            <div class="card">
              <div style="aspect-ratio: 16/10; background: url('https://images.unsplash.com/photo-1521737852567-6949f3f9f2b5?w=1600&q=80&auto=format&fit=crop') center/cover;"></div>
              <div class="card-body">
                <div class="eyebrow">CASE STUDY</div>
                <h3 style="margin: 10px 0 6px; font-size: 16px;">3 alasan word-of-mouth tetap mengalahkan paid media</h3>
                <p class="small muted mb-0">5 menit baca · Adi Pratama</p>
              </div>
            </div>
          </a>
        </div>
      </div>
    </div>

    {mega_footer()}
  </div>
</section>'''
    return head + body + chrome_close()


def page_dispute():
    extra = '''<style>
    .dispute-hero { padding: 96px 40px 64px; text-align: center; background: linear-gradient(180deg, var(--grey-50) 0%, #fff 100%); }
    .dispute-hero h1 { font-size: 48px; line-height: 1.1; letter-spacing: -0.025em; margin: 14px 0 16px; }
    .dispute-hero .lead { font-size: 19px; color: var(--muted); max-width: 720px; margin: 0 auto; line-height: 1.6; }
    .process-steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 48px; max-width: 1100px; margin-left: auto; margin-right: auto; padding: 0 40px; }
    .process-step { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 28px 22px; position: relative; }
    .process-step .num { width: 36px; height: 36px; border-radius: 50%; background: var(--accent-soft); color: var(--accent); display: inline-flex; align-items: center; justify-content: center; font-family: var(--font-display); font-weight: 800; font-size: 16px; margin-bottom: 12px; }
    .process-step h4 { margin: 0 0 6px; font-size: 15px; }
    .process-step .time { font-size: 12px; color: var(--accent); font-weight: 600; margin-top: 10px; padding-top: 10px; border-top: 1px dashed var(--line); }
    .dispute-form { max-width: 720px; margin: 0 auto; padding: 80px 40px; }
    .dispute-form .form-card { background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 32px; box-shadow: var(--shadow-1); }
    .dispute-form .form-row { margin-bottom: 18px; }
    .dispute-form label { display: block; font-size: 13px; font-weight: 600; margin-bottom: 6px; color: var(--ink); }
    .dispute-form input, .dispute-form select, .dispute-form textarea { width: 100%; padding: 12px 14px; border: 1px solid var(--line); border-radius: 10px; font-family: var(--font-body); font-size: 14px; background: #fff; }
    .dispute-form input:focus, .dispute-form select:focus, .dispute-form textarea:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 4px rgba(11,95,224,0.08); }
    .dispute-form textarea { min-height: 120px; resize: vertical; }
    .file-upload { border: 2px dashed var(--line); border-radius: 12px; padding: 24px; text-align: center; cursor: pointer; transition: all 0.15s; }
    .file-upload:hover { border-color: var(--accent); background: var(--accent-soft); }
    .trust-msg { background: var(--accent-soft); border: 1px solid #c8d8f7; border-radius: 12px; padding: 20px; display: flex; gap: 14px; align-items: flex-start; margin-bottom: 32px; }
    .trust-msg .ico { width: 40px; height: 40px; border-radius: 50%; background: var(--accent); color: #fff; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  </style>'''
    head = chrome('Laporkan Sengketa — Resonansi', '', 'dispute.html', extra)
    body = f'''<section class="screen">
  <div class="frame">

    {web_header(active='')}

    <div class="dispute-hero">
      <div class="container">
        <div class="eyebrow">RESOLUSI SENGKETA</div>
        <h1>Laporkan Sengketa</h1>
        <p class="lead">Tim mediator independen kami merespons dalam <strong>24 jam</strong>. Untuk semua pihak — advocate, klien, atau publik yang melihat ketidakberesan.</p>
      </div>

      <div class="process-steps">
        <div class="process-step">
          <div class="num">1</div>
          <h4>Laporkan</h4>
          <p class="small muted mb-0">Anda submit form di bawah dengan bukti pendukung (screenshot, kontrak, link).</p>
          <div class="time">Hari 0</div>
        </div>
        <div class="process-step">
          <div class="num">2</div>
          <h4>Investigasi</h4>
          <p class="small muted mb-0">Tim Trust & Safety mengaudit transaksi, konten, dan audit trail dari kedua pihak.</p>
          <div class="time">Hari 1–3</div>
        </div>
        <div class="process-step">
          <div class="num">3</div>
          <h4>Mediasi</h4>
          <p class="small muted mb-0">Mediator independen memfasilitasi diskusi dan mencari resolusi yang adil.</p>
          <div class="time">Hari 3–7</div>
        </div>
        <div class="process-step">
          <div class="num">4</div>
          <h4>Arbitrase</h4>
          <p class="small muted mb-0">Jika tidak mencapai kesepakatan, panel arbitrase 3 orang memberikan putusan final.</p>
          <div class="time">Hari 7–14</div>
        </div>
      </div>
    </div>

    <!-- Form -->
    <div class="dispute-form">
      <div class="trust-msg">
        <div class="ico"><svg width="20" height="20"><use href="#i-shield"/></svg></div>
        <div>
          <strong>Identitas Anda dilindungi.</strong>
          <p class="small muted mb-0" style="margin-top: 4px; line-height: 1.55;">
            Kami tidak akan share data Anda ke pihak lawan tanpa persetujuan. Semua komunikasi melalui platform yang ter-encrypt.
          </p>
        </div>
      </div>

      <div class="form-card">
        <h3 style="margin: 0 0 4px;">Form Laporan Sengketa</h3>
        <p class="small muted" style="margin: 0 0 24px;">Semua field dengan tanda * wajib diisi.</p>

        <form onsubmit="event.preventDefault(); alert('Laporan terkirim. Tim kami akan kontak Anda dalam 24 jam ke email yang terdaftar.');">
          <div class="form-row">
            <label>Jenis Sengketa *</label>
            <select required>
              <option>-- Pilih jenis --</option>
              <option>Pembayaran tertahan / tidak diterima</option>
              <option selected>Konten gagal verifikasi</option>
              <option>Disclosure tidak dilampirkan</option>
              <option>Konten melanggar guideline</option>
              <option>Bot / fake engagement</option>
              <option>Pelanggaran kontrak</option>
              <option>Lainnya</option>
            </select>
          </div>

          <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div>
              <label>Kampanye / Brief ID</label>
              <input type="text" placeholder="Contoh: BRF-2026-0421" value="BRF-2026-0421">
            </div>
            <div>
              <label>Pihak Lawan</label>
              <input type="text" placeholder="@username atau nama brand" value="Falcon Pictures">
            </div>
          </div>

          <div class="form-row">
            <label>Deskripsi Sengketa *</label>
            <textarea placeholder="Ceritakan kronologi lengkap. Sertakan tanggal, jam, dan detail spesifik." required>Saya menyelesaikan deliverable sesuai brief (1 TikTok + 1 Reel + 3 IG Story) pada 16 April 2026. Klien menolak dengan alasan "kualitas tidak sesuai" tanpa memberikan detail bagian mana yang bermasalah. Pembayaran Rp 850.000 ditahan sejak 18 April...</textarea>
            <div class="small muted" style="margin-top: 4px;">Minimal 100 karakter. Jelaskan apa yang terjadi, kapan, dan apa yang Anda harapkan.</div>
          </div>

          <div class="form-row">
            <label>Resolusi yang Diharapkan</label>
            <select>
              <option>-- Pilih --</option>
              <option selected>Pembayaran dirilis sesuai kontrak</option>
              <option>Klarifikasi alasan penolakan</option>
              <option>Kesempatan revisi konten</option>
              <option>Pembayaran parsial (50%)</option>
              <option>Mediasi tanpa klaim spesifik</option>
            </select>
          </div>

          <div class="form-row">
            <label>Bukti / Lampiran (opsional)</label>
            <div class="file-upload">
              <svg width="32" height="32" style="color: var(--muted);"><use href="#i-attach"/></svg>
              <div style="margin-top: 8px; font-size: 13.5px; font-weight: 600;">Klik atau drop file di sini</div>
              <div class="small muted" style="margin-top: 4px;">Screenshot, kontrak, link konten — max 5 file, 10MB each. PNG, JPG, PDF.</div>
            </div>
          </div>

          <div class="form-row" style="margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--line);">
            <label style="display: flex; gap: 10px; cursor: pointer; font-weight: 500;">
              <input type="checkbox" required style="accent-color: var(--accent); margin-top: 3px;">
              <span class="small">Saya menyatakan informasi di atas benar dan saya bersedia bekerja sama dengan tim mediator Resonansi sesuai <a href="#" style="color: var(--accent);">SOP Resolusi Sengketa</a>.</span>
            </label>
          </div>

          <button type="submit" class="btn lg" style="width: 100%; justify-content: center;">Kirim Laporan Sengketa →</button>
          <p class="small muted center" style="margin-top: 12px;">Anda akan mendapat email konfirmasi dan dispute ID dalam 5 menit.</p>
        </form>
      </div>

      <div style="margin-top: 32px; padding: 20px; background: var(--grey-50); border-radius: 12px;">
        <strong style="font-size: 14px;">Butuh bantuan langsung?</strong>
        <p class="small muted" style="margin: 4px 0 8px;">Untuk kasus urgent (pembayaran &gt; Rp 5 jt, ancaman hukum), kontak hotline dispute.</p>
        <div class="row-tight">
          <a href="contact.html" class="btn neutral small">📞 Hotline 24/7</a>
          <a href="trust.html" class="btn ghost small">Baca panduan Trust & Safety →</a>
        </div>
      </div>
    </div>

    {mega_footer()}
  </div>
</section>'''
    return head + body + chrome_close()


def page_career():
    extra = '''<style>
    .career-hero { padding: 96px 40px 64px; background: linear-gradient(180deg, var(--accent-soft) 0%, #fff 100%); }
    .career-hero h1 { font-size: 56px; line-height: 1.05; letter-spacing: -0.03em; margin: 14px 0 24px; max-width: 720px; }
    .career-hero .lead { font-size: 19px; color: var(--muted); max-width: 660px; line-height: 1.55; }
    .career-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 48px; max-width: 720px; }
    .career-stat { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 24px; box-shadow: var(--shadow-1); }
    .career-stat .num { font-family: var(--font-display); font-size: 36px; font-weight: 800; color: var(--accent); line-height: 1; letter-spacing: -0.02em; }
    .career-stat .label { font-size: 13px; color: var(--muted); margin-top: 8px; }
    .values-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 40px; }
    .value-card { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 28px 22px; }
    .value-card .ico { width: 44px; height: 44px; border-radius: 12px; background: var(--accent-soft); color: var(--accent); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 14px; }
    .value-card h4 { margin: 0 0 6px; font-size: 15px; letter-spacing: -0.005em; }
    .jobs-table { background: #fff; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-1); }
    .job-row { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr auto; gap: 16px; padding: 18px 20px; border-bottom: 1px solid var(--grey-100); align-items: center; }
    .job-row:last-child { border: 0; }
    .job-row:hover { background: var(--grey-50); }
    .job-row .pos { font-weight: 600; font-size: 14.5px; }
    .job-row .small-meta { font-size: 12.5px; color: var(--muted); }
    .life-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-top: 32px; }
    .life-grid img { width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 12px; }
  </style>'''
    head = chrome('Karir — Resonansi', '', 'career.html', extra)
    body = f'''<section class="screen">
  <div class="frame">

    {web_header(active='')}

    <div class="career-hero">
      <div class="container">
        <div class="eyebrow">KARIR</div>
        <h1>Bangun Resonansi bersama kami.</h1>
        <p class="lead">Kami membangun infrastruktur untuk menjadikan influence accountable. Itu artinya kami butuh orang yang peduli dengan craft, integritas, dan dampak nyata bagi 270 juta orang Indonesia.</p>

        <div class="career-stats">
          <div class="career-stat"><div class="num">37</div><div class="label">Anggota tim aktif</div></div>
          <div class="career-stat"><div class="num">4.9★</div><div class="label">Culture rating (Kunci)</div></div>
          <div class="career-stat"><div class="num">14</div><div class="label">Fungsi yang sedang hire</div></div>
        </div>

        <div class="row-tight" style="margin-top: 32px;">
          <a class="btn lg" href="#open-positions">Lihat Posisi Tersedia ↓</a>
          <a class="btn neutral lg" href="about.html">Kenal Tim Founding →</a>
        </div>
      </div>
    </div>

    <!-- Values -->
    <div class="mkt-section">
      <div class="container">
        <div class="eyebrow">VALUES</div>
        <h2 class="title">Apa yang kami percayai.</h2>

        <div class="values-grid">
          <div class="value-card">
            <div class="ico"><svg width="22" height="22"><use href="#i-users"/></svg></div>
            <h4>Suara Setara</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">Tier 5 community lead sama valuable dengan Tier 1 celebrity. Kami build untuk kedua-duanya.</p>
          </div>
          <div class="value-card">
            <div class="ico"><svg width="22" height="22"><use href="#i-shield"/></svg></div>
            <h4>Compliance First</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">Trust adalah produk. Kami invest besar di audit trail, KYC, dan disclosure — bahkan ketika tidak diminta.</p>
          </div>
          <div class="value-card">
            <div class="ico"><svg width="22" height="22"><use href="#i-zap"/></svg></div>
            <h4>Mobile-Craft</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">Mayoritas user kami mobile-first. Setiap fitur harus excellent di Android low-end & koneksi 3G.</p>
          </div>
          <div class="value-card">
            <div class="ico"><svg width="22" height="22"><use href="#i-play"/></svg></div>
            <h4>Bias toward Action</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">Daripada committee 3 minggu, kami prefer prototype 3 hari dan iterate dari data nyata.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Open Positions -->
    <div class="mkt-section alt" id="open-positions">
      <div class="container">
        <div class="eyebrow">POSISI TERSEDIA</div>
        <h2 class="title">Bergabung sekarang.</h2>
        <p class="lead">Semua posisi base di Jakarta. Hybrid 3 hari di office (SCBD), 2 hari remote. Open untuk pindahan dari Bandung, Surabaya, Yogya.</p>

        <div class="jobs-table" style="margin-top: 32px;">
          <div class="job-row" style="background: var(--grey-50); font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted);">
            <div>Posisi</div>
            <div>Tim</div>
            <div>Lokasi</div>
            <div>Tipe</div>
            <div></div>
          </div>
          <div class="job-row">
            <div>
              <div class="pos">Senior Backend Engineer</div>
              <div class="small-meta">Go, PostgreSQL, gRPC · 5+ tahun pengalaman</div>
            </div>
            <div class="small-meta">Engineering</div>
            <div class="small-meta">Jakarta · Hybrid</div>
            <div><span class="pill" style="background: var(--accent-soft); color: var(--accent); border-color: #c8d8f7;">Full-time</span></div>
            <div><a class="btn neutral small" href="contact.html">Apply →</a></div>
          </div>
          <div class="job-row">
            <div>
              <div class="pos">ML / Matching Engine</div>
              <div class="small-meta">Python, recommender systems, embedding · 3+ tahun</div>
            </div>
            <div class="small-meta">Engineering</div>
            <div class="small-meta">Jakarta · Hybrid</div>
            <div><span class="pill" style="background: var(--accent-soft); color: var(--accent); border-color: #c8d8f7;">Full-time</span></div>
            <div><a class="btn neutral small" href="contact.html">Apply →</a></div>
          </div>
          <div class="job-row">
            <div>
              <div class="pos">Compliance Officer (Bawaslu / PKPU)</div>
              <div class="small-meta">SH/SHumum, paham KPU/Bawaslu workflow · 5+ tahun</div>
            </div>
            <div class="small-meta">Trust & Safety</div>
            <div class="small-meta">Jakarta · On-site</div>
            <div><span class="pill" style="background: var(--accent-soft); color: var(--accent); border-color: #c8d8f7;">Full-time</span></div>
            <div><a class="btn neutral small" href="contact.html">Apply →</a></div>
          </div>
          <div class="job-row">
            <div>
              <div class="pos">Business Development — Politik</div>
              <div class="small-meta">Network ke tim sukses, paham regulasi pemilu</div>
            </div>
            <div class="small-meta">Sales / BD</div>
            <div class="small-meta">Jakarta · Hybrid</div>
            <div><span class="pill" style="background: var(--accent-soft); color: var(--accent); border-color: #c8d8f7;">Full-time</span></div>
            <div><a class="btn neutral small" href="contact.html">Apply →</a></div>
          </div>
          <div class="job-row">
            <div>
              <div class="pos">Product Designer (Sr.)</div>
              <div class="small-meta">Figma, mobile-first, design system · 4+ tahun</div>
            </div>
            <div class="small-meta">Design</div>
            <div class="small-meta">Jakarta · Hybrid</div>
            <div><span class="pill warn">Contract → Full-time</span></div>
            <div><a class="btn neutral small" href="contact.html">Apply →</a></div>
          </div>
          <div class="job-row">
            <div>
              <div class="pos">Account Manager (Enterprise)</div>
              <div class="small-meta">Manage 5–8 client tier-1, target Rp 2 M/qtr</div>
            </div>
            <div class="small-meta">Customer Success</div>
            <div class="small-meta">Jakarta · Hybrid</div>
            <div><span class="pill" style="background: var(--accent-soft); color: var(--accent); border-color: #c8d8f7;">Full-time</span></div>
            <div><a class="btn neutral small" href="contact.html">Apply →</a></div>
          </div>
        </div>

        <div style="margin-top: 28px; padding: 20px 24px; background: var(--accent-soft); border-radius: 12px; display: flex; gap: 16px; align-items: center;">
          <div class="ico-circle" style="background: var(--accent); color: #fff; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
            <svg width="20" height="20"><use href="#i-mail"/></svg>
          </div>
          <div style="flex:1;">
            <strong>Tidak lihat posisi yang sesuai?</strong>
            <div class="small muted" style="margin-top: 2px;">Kirim resume Anda — kami selalu welcoming exceptional talent untuk future roles.</div>
          </div>
          <a class="btn" href="contact.html">Kirim Resume →</a>
        </div>
      </div>
    </div>

    <!-- Life at Resonansi -->
    <div class="mkt-section">
      <div class="container">
        <div class="eyebrow">LIFE AT RESONANSI</div>
        <h2 class="title">Bekerja di sini.</h2>
        <p class="lead">Office SCBD (Equity Tower), 4.9 culture rating, opsi remote 2 hari/minggu, equity untuk semua, 28 hari leave + 14 hari WFA.</p>

        <div class="life-grid">
          <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=1600&q=80&auto=format&fit=crop" alt="Coworking">
          <img src="https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=1600&q=80&auto=format&fit=crop" alt="Team meeting">
          <img src="https://images.unsplash.com/photo-1521737852567-6949f3f9f2b5?w=1600&q=80&auto=format&fit=crop" alt="Coffee discussion">
          <img src="https://images.unsplash.com/photo-1551434678-e076c223a692?w=1600&q=80&auto=format&fit=crop" alt="Laptop work">
        </div>

        <div class="row-tight" style="margin-top: 40px; justify-content: center;">
          <a class="btn lg" href="#open-positions">Lihat Semua Posisi (6 open) →</a>
        </div>
      </div>
    </div>

    {mega_footer()}
  </div>
</section>'''
    return head + body + chrome_close()


def page_press():
    extra = '''<style>
    .press-hero { padding: 96px 40px 56px; background: linear-gradient(180deg, var(--grey-50) 0%, #fff 100%); text-align: center; }
    .press-hero h1 { font-size: 56px; line-height: 1.05; letter-spacing: -0.03em; margin: 14px 0 16px; }
    .press-hero .lead { font-size: 19px; color: var(--muted); max-width: 720px; margin: 0 auto; line-height: 1.55; }
    .contact-card { background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 32px; max-width: 720px; margin: 40px auto 0; box-shadow: var(--shadow-1); display: grid; grid-template-columns: 80px 1fr auto; gap: 20px; align-items: center; }
    .contact-card img { width: 80px; height: 80px; border-radius: 50%; object-fit: cover; }
    .logos-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 32px; }
    .logo-card { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 32px 20px; text-align: center; transition: all 0.15s; }
    .logo-card:hover { border-color: var(--accent); box-shadow: 0 4px 12px rgba(11,95,224,0.08); }
    .logo-card .preview { font-family: var(--font-display); font-size: 26px; font-weight: 800; letter-spacing: -0.02em; padding: 24px; border-radius: 10px; margin-bottom: 12px; }
    .preview.dark { background: var(--ink); color: #fff; }
    .preview.light { background: #fff; color: var(--ink); border: 1px solid var(--line); }
    .preview.blue { background: var(--accent); color: #fff; }
    .preview.amber { background: #FFB400; color: var(--ink); }
    .coverage-list { background: #fff; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
    .coverage-row { display: grid; grid-template-columns: 120px 1fr auto; gap: 20px; padding: 20px 24px; border-bottom: 1px solid var(--grey-100); align-items: center; }
    .coverage-row:last-child { border: 0; }
    .coverage-outlet { font-family: var(--font-display); font-weight: 700; font-size: 14px; padding: 8px 12px; background: var(--grey-100); border-radius: 8px; text-align: center; letter-spacing: 0.02em; }
    .founders-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 32px; }
    .founder-card { background: #fff; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
    .founder-card img { width: 100%; aspect-ratio: 1; object-fit: cover; }
    .founder-card .body { padding: 14px; text-align: center; }
    .release-card { background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 20px 24px; margin-bottom: 12px; display: flex; align-items: center; gap: 16px; }
  </style>'''
    head = chrome('Press & Media — Resonansi', '', 'press.html', extra)
    body = f'''<section class="screen">
  <div class="frame">

    {web_header(active='')}

    <div class="press-hero">
      <div class="container">
        <div class="eyebrow">PRESS &amp; MEDIA</div>
        <h1>Press &amp; Media Kit</h1>
        <p class="lead">Semua yang Anda butuhkan untuk meliput Resonansi: logo, foto founder, fakta cepat, dan press release arsip.</p>
      </div>

      <!-- Press contact -->
      <div class="contact-card">
        <img src="https://i.pravatar.cc/150?img=44" alt="Lia Andini">
        <div>
          <div class="eyebrow">KONTAK PRESS</div>
          <strong style="font-size: 16px; display: block; margin-top: 4px;">Lia Andini</strong>
          <div class="small muted">Head of Communications · Resonansi</div>
          <div class="small" style="margin-top: 6px;">📧 press@resonansi.id · 📱 +62 813 8888 4321</div>
        </div>
        <a href="contact.html" class="btn">Email Press Team →</a>
      </div>
    </div>

    <!-- Logo downloads -->
    <div class="mkt-section">
      <div class="container">
        <div class="eyebrow">LOGO &amp; BRAND ASSETS</div>
        <h2 class="title">Download logo Resonansi.</h2>
        <p class="lead">4 variant tersedia. Format PNG (transparent) dan SVG. Mohon pakai logo dengan clear-space minimum sesuai brand guideline.</p>

        <div class="logos-grid">
          <div class="logo-card">
            <div class="preview dark">RESONANSI</div>
            <strong style="font-size: 14px; display: block;">Logo Primary (Dark)</strong>
            <div class="small muted">PNG · SVG · 240KB</div>
            <a class="btn ghost small" style="margin-top: 8px; padding-left: 0;">Download ↓</a>
          </div>
          <div class="logo-card">
            <div class="preview light">RESONANSI</div>
            <strong style="font-size: 14px; display: block;">Logo Secondary (Light)</strong>
            <div class="small muted">PNG · SVG · 220KB</div>
            <a class="btn ghost small" style="margin-top: 8px; padding-left: 0;">Download ↓</a>
          </div>
          <div class="logo-card">
            <div class="preview blue">RESONANSI</div>
            <strong style="font-size: 14px; display: block;">Logo Brand Blue</strong>
            <div class="small muted">PNG · SVG · 260KB</div>
            <a class="btn ghost small" style="margin-top: 8px; padding-left: 0;">Download ↓</a>
          </div>
          <div class="logo-card">
            <div class="preview amber">RESONANSI</div>
            <strong style="font-size: 14px; display: block;">Logo Accent Amber</strong>
            <div class="small muted">PNG · SVG · 260KB</div>
            <a class="btn ghost small" style="margin-top: 8px; padding-left: 0;">Download ↓</a>
          </div>
        </div>

        <div style="margin-top: 32px; padding: 20px; background: var(--accent-soft); border-radius: 12px; display: flex; gap: 16px; align-items: center;">
          <svg width="32" height="32" style="color: var(--accent);"><use href="#i-shield"/></svg>
          <div style="flex:1;">
            <strong>Brand Guidelines (PDF · 4.2 MB)</strong>
            <div class="small muted">Color palette, typography, spacing, do's & don'ts. Wajib baca sebelum publikasi.</div>
          </div>
          <a class="btn" href="design-system.html">Download Brand Book →</a>
        </div>
      </div>
    </div>

    <!-- Recent coverage -->
    <div class="mkt-section alt">
      <div class="container">
        <div class="eyebrow">RECENT COVERAGE</div>
        <h2 class="title">Resonansi di media.</h2>

        <div class="coverage-list" style="margin-top: 32px;">
          <div class="coverage-row">
            <div class="coverage-outlet">TECH IN ASIA</div>
            <div>
              <strong style="font-size: 14.5px;">Resonansi Raised Rp 28 Billion Series Seed to Build Accountable Influence Marketplace</strong>
              <div class="small muted" style="margin-top: 4px;">"...the company's approach to compliance is a clear differentiator in a market that has long been opaque."</div>
            </div>
            <div class="small muted">22 Apr 2026</div>
          </div>
          <div class="coverage-row">
            <div class="coverage-outlet">KOMPAS</div>
            <div>
              <strong style="font-size: 14.5px;">Mengubah Wajah "Buzzer" Politik: Startup Resonansi Tawarkan Audit Trail Publik</strong>
              <div class="small muted" style="margin-top: 4px;">"Dengan compliance Bawaslu yang built-in, Resonansi mencoba mengakhiri era kampanye opaque..."</div>
            </div>
            <div class="small muted">15 Mar 2026</div>
          </div>
          <div class="coverage-row">
            <div class="coverage-outlet">DETIKINET</div>
            <div>
              <strong style="font-size: 14.5px;">12.500 Advocate Verified: Bagaimana Resonansi Menggerakkan Word-of-Mouth Untuk Film</strong>
              <div class="small muted" style="margin-top: 4px;">"Salah satu film yang menggunakan platform ini melihat okupansi naik dari 34% jadi 68%."</div>
            </div>
            <div class="small muted">28 Feb 2026</div>
          </div>
          <div class="coverage-row">
            <div class="coverage-outlet">DAILYSOCIAL</div>
            <div>
              <strong style="font-size: 14.5px;">Founder Profile: Sari Wijaya on Building Resonansi's Matching Engine</strong>
              <div class="small muted" style="margin-top: 4px;">"...the technical challenge is matching diversity, not just volume."</div>
            </div>
            <div class="small muted">10 Feb 2026</div>
          </div>
          <div class="coverage-row">
            <div class="coverage-outlet">JAKPOST</div>
            <div>
              <strong style="font-size: 14.5px;">Indonesia's Rp 28 Trillion Influence Market — and the Startup Trying to Clean It Up</strong>
              <div class="small muted" style="margin-top: 4px;">"Resonansi positions itself as the 'Big Four-audited' equivalent for the influence industry."</div>
            </div>
            <div class="small muted">22 Jan 2026</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Founder photos -->
    <div class="mkt-section">
      <div class="container">
        <div class="eyebrow">FOUNDER PHOTOS</div>
        <h2 class="title">Foto founder & tim.</h2>
        <p class="lead">Hi-res photos untuk press. Klik untuk download (PNG, ~3000x3000px).</p>

        <div class="founders-grid">
          <div class="founder-card">
            <img src="https://i.pravatar.cc/600?img=33" alt="Adi Pratama">
            <div class="body"><strong>Adi Pratama</strong><div class="small muted">CEO · Co-Founder</div></div>
          </div>
          <div class="founder-card">
            <img src="https://i.pravatar.cc/600?img=47" alt="Sari Wijaya">
            <div class="body"><strong>Sari Wijaya</strong><div class="small muted">CTO · Co-Founder</div></div>
          </div>
          <div class="founder-card">
            <img src="https://i.pravatar.cc/600?img=12" alt="Bayu Hidayat">
            <div class="body"><strong>Bayu Hidayat</strong><div class="small muted">CPO</div></div>
          </div>
          <div class="founder-card">
            <img src="https://i.pravatar.cc/600?img=44" alt="Maya Putri">
            <div class="body"><strong>Maya Putri, SH</strong><div class="small muted">Head of Trust</div></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Press releases -->
    <div class="mkt-section alt">
      <div class="container">
        <div class="eyebrow">PRESS RELEASE ARCHIVE</div>
        <h2 class="title">Press release resmi.</h2>

        <div style="margin-top: 32px;">
          <div class="release-card">
            <svg width="20" height="20" style="color: var(--accent);"><use href="#i-attach"/></svg>
            <div style="flex:1;">
              <strong style="font-size: 15px;">Resonansi Raises USD 1.8M Seed Round to Build Indonesia's Accountable Influence Infrastructure</strong>
              <div class="small muted" style="margin-top: 4px;">PR · 22 April 2026 · 1.2 MB PDF</div>
            </div>
            <a class="btn ghost small" style="padding-left: 0;">Download →</a>
          </div>
          <div class="release-card">
            <svg width="20" height="20" style="color: var(--accent);"><use href="#i-attach"/></svg>
            <div style="flex:1;">
              <strong style="font-size: 15px;">Resonansi Launches Bawaslu-Compliance Module for 2027 Pilkada Campaign Teams</strong>
              <div class="small muted" style="margin-top: 4px;">PR · 14 Maret 2026 · 980 KB PDF</div>
            </div>
            <a class="btn ghost small" style="padding-left: 0;">Download →</a>
          </div>
          <div class="release-card">
            <svg width="20" height="20" style="color: var(--accent);"><use href="#i-attach"/></svg>
            <div style="flex:1;">
              <strong style="font-size: 15px;">12.500 Verified Advocates: Resonansi Reaches Major Milestone in Indonesia's Influence Marketplace</strong>
              <div class="small muted" style="margin-top: 4px;">PR · 6 Februari 2026 · 1.4 MB PDF</div>
            </div>
            <a class="btn ghost small" style="padding-left: 0;">Download →</a>
          </div>
        </div>
      </div>
    </div>

    {mega_footer()}
  </div>
</section>'''
    return head + body + chrome_close()


def main():
    pages = [
        ('case-study-detail.html', page_case_study_detail),
        ('blog-detail.html', page_blog_detail),
        ('dispute.html', page_dispute),
        ('career.html', page_career),
        ('press.html', page_press),
    ]
    for rel, fn in pages:
        write_page(rel, fn())
    print(f'\n  → wrote {len(pages)} pages (batch 2)')


if __name__ == '__main__':
    main()
