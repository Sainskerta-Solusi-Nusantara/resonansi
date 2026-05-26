"""Batch 3: trust-audit, advocate/tax-receipt, welcome, notifications"""
import sys
sys.path.insert(0, '/Users/haimac/buzzer/site')
from _build_new_pages import chrome, chrome_close, web_header, mega_footer, write_page


def page_trust_audit():
    extra = '''<style>
    .ta-hero { padding: 96px 40px 56px; background: linear-gradient(180deg, var(--ink) 0%, #1c2e4a 100%); color: #fff; text-align: center; }
    .ta-hero h1 { font-size: 48px; line-height: 1.1; letter-spacing: -0.025em; color: #fff; margin: 14px 0 16px; }
    .ta-hero .lead { font-size: 19px; opacity: 0.85; max-width: 720px; margin: 0 auto; line-height: 1.55; }
    .ta-hero .eyebrow { color: #FFB400; opacity: 1; }
    .ta-trust-row { display: inline-flex; align-items: center; gap: 10px; margin-top: 24px; padding: 8px 18px; background: rgba(255,255,255,0.08); border-radius: 999px; font-size: 13px; }
    .ta-trust-row .dot { width: 8px; height: 8px; border-radius: 50%; background: #16a34a; box-shadow: 0 0 0 3px rgba(22,163,74,0.25); }
    .ta-filters { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 18px 22px; margin: -32px auto 32px; max-width: 1200px; display: grid; grid-template-columns: 1.5fr 1fr 1fr auto; gap: 14px; align-items: center; position: relative; z-index: 5; box-shadow: 0 12px 36px rgba(15,30,60,0.08); }
    .ta-filters .field-label { font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); margin-bottom: 4px; }
    .ta-filters select, .ta-filters input { width: 100%; padding: 10px 12px; border: 1px solid var(--line); border-radius: 10px; font-family: var(--font-body); font-size: 13.5px; background: #fff; }
    .ta-table { background: #fff; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-1); }
    .ta-table table { width: 100%; border-collapse: collapse; }
    .ta-table th { font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); padding: 14px 20px; text-align: left; border-bottom: 1px solid var(--line); background: var(--grey-50); }
    .ta-table td { padding: 16px 20px; border-bottom: 1px solid var(--grey-100); font-size: 13.5px; vertical-align: top; }
    .ta-table tr:last-child td { border-bottom: 0; }
    .ta-table tr:hover { background: var(--grey-50); }
    .compl-bar { background: var(--grey-100); border-radius: 4px; height: 6px; overflow: hidden; margin-top: 4px; }
    .compl-bar > div { height: 100%; border-radius: 4px; }
    .compl-good { background: #16a34a; }
    .compl-warn { background: #FFB400; }
    .compl-bad { background: #d4404a; }
    .ta-explainer { background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 40px; margin-top: 48px; box-shadow: var(--shadow-1); }
    .ta-explainer-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 24px; }
    .ta-explain-step .num { width: 36px; height: 36px; border-radius: 50%; background: var(--accent); color: #fff; display: inline-flex; align-items: center; justify-content: center; font-family: var(--font-display); font-weight: 800; margin-bottom: 12px; }
    .ta-pillar { background: linear-gradient(135deg, var(--accent) 0%, #093F94 100%); color: #fff; border-radius: 16px; padding: 40px; text-align: center; margin-top: 40px; }
    .ta-pillar h3 { font-family: var(--font-display); color: #FFB400; font-size: 26px; margin: 0 0 12px; letter-spacing: -0.01em; }
  </style>'''
    head = chrome('Trust Audit Publik · Kampanye Politik — Resonansi', '', 'trust-audit.html', extra)
    body = f'''<section class="screen">
  <div class="frame">

    {web_header(active='')}

    <div class="ta-hero">
      <div class="container">
        <div class="eyebrow">AUDIT TRAIL PUBLIK</div>
        <h1>Transparansi Kampanye Politik Berbayar</h1>
        <p class="lead">Setiap kampanye politik berbayar di Resonansi terdaftar di sini. Publik bisa melihat sponsor, advocate, konten yang diproduksi, dan compliance disclosure — real-time.</p>
        <div class="ta-trust-row">
          <span class="dot"></span>
          <span><strong>Live</strong> · Update otomatis · Compliance Bawaslu 2024 standard</span>
        </div>
      </div>
    </div>

    <!-- Filters -->
    <div class="ta-filters">
      <div>
        <div class="field-label">Kandidat / Sponsor</div>
        <select>
          <option>Semua kandidat (12)</option>
          <option>Kandidat A — Pilkada Jakarta</option>
          <option>Kandidat B — Pilkada Jabar</option>
          <option>Kandidat C — Pilgub Sumut</option>
        </select>
      </div>
      <div>
        <div class="field-label">Periode</div>
        <select>
          <option>April 2026</option>
          <option>Maret 2026</option>
          <option>Februari 2026</option>
          <option>2025 (full year)</option>
        </select>
      </div>
      <div>
        <div class="field-label">Region</div>
        <select>
          <option>Semua region</option>
          <option>Jabodetabek</option>
          <option>Jawa Barat</option>
          <option>Jawa Tengah</option>
          <option>Jawa Timur</option>
          <option>Sumatera</option>
          <option>Indonesia Timur</option>
        </select>
      </div>
      <div style="align-self: flex-end;">
        <a class="btn">Filter Hasil</a>
      </div>
    </div>

    <!-- Table -->
    <div class="container">
      <div class="ta-table">
        <table>
          <thead>
            <tr>
              <th>Judul Kampanye</th>
              <th>Sponsor</th>
              <th>Region</th>
              <th>Advocate</th>
              <th>Konten</th>
              <th>Disclosure</th>
              <th>Periode</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Pencitraan Kandidat A — Image Building</strong><br><span class="small muted">PLT-2026-0142</span></td>
              <td>Tim Sukses Kandidat A<br><span class="small muted">PT Sahabat Demokrasi</span></td>
              <td>Jabodetabek</td>
              <td>342</td>
              <td>1.847</td>
              <td>
                <strong style="color: #16a34a;">100%</strong>
                <div class="compl-bar"><div class="compl-good" style="width: 100%;"></div></div>
              </td>
              <td><span class="small">14–28 Apr 2026</span></td>
              <td><a class="btn ghost small" style="padding-left: 0;">Lihat Trail →</a></td>
            </tr>
            <tr>
              <td><strong>Sosialisasi Program Pendidikan</strong><br><span class="small muted">PLT-2026-0138</span></td>
              <td>Tim Sukses Kandidat B<br><span class="small muted">Yayasan Cerdas Jabar</span></td>
              <td>Jawa Barat</td>
              <td>218</td>
              <td>892</td>
              <td>
                <strong style="color: #16a34a;">100%</strong>
                <div class="compl-bar"><div class="compl-good" style="width: 100%;"></div></div>
              </td>
              <td><span class="small">10–24 Apr 2026</span></td>
              <td><a class="btn ghost small" style="padding-left: 0;">Lihat Trail →</a></td>
            </tr>
            <tr>
              <td><strong>Mobilisasi Pemilih Muda — Pilkada</strong><br><span class="small muted">PLT-2026-0131</span></td>
              <td>Tim Sukses Kandidat C<br><span class="small muted">Aliansi Sumut Maju</span></td>
              <td>Sumatera Utara</td>
              <td>567</td>
              <td>2.314</td>
              <td>
                <strong style="color: #FFB400;">98%</strong>
                <div class="compl-bar"><div class="compl-warn" style="width: 98%;"></div></div>
              </td>
              <td><span class="small">1–30 Apr 2026</span></td>
              <td><a class="btn ghost small" style="padding-left: 0;">Lihat Trail →</a></td>
            </tr>
            <tr>
              <td><strong>Awareness Visi-Misi Kandidat D</strong><br><span class="small muted">PLT-2026-0127</span></td>
              <td>Tim Sukses Kandidat D<br><span class="small muted">PT Pilihan Rakyat</span></td>
              <td>Jawa Timur</td>
              <td>198</td>
              <td>743</td>
              <td>
                <strong style="color: #16a34a;">100%</strong>
                <div class="compl-bar"><div class="compl-good" style="width: 100%;"></div></div>
              </td>
              <td><span class="small">5–19 Apr 2026</span></td>
              <td><a class="btn ghost small" style="padding-left: 0;">Lihat Trail →</a></td>
            </tr>
            <tr>
              <td><strong>Counter-Disinformasi Tim Sukses E</strong><br><span class="small muted">PLT-2026-0119</span></td>
              <td>Tim Sukses Kandidat E<br><span class="small muted">Yayasan Demokrasi Bersih</span></td>
              <td>Jawa Tengah</td>
              <td>124</td>
              <td>487</td>
              <td>
                <strong style="color: #16a34a;">100%</strong>
                <div class="compl-bar"><div class="compl-good" style="width: 100%;"></div></div>
              </td>
              <td><span class="small">8–22 Apr 2026</span></td>
              <td><a class="btn ghost small" style="padding-left: 0;">Lihat Trail →</a></td>
            </tr>
            <tr>
              <td><strong>Sosialisasi Calon Walikota F</strong><br><span class="small muted">PLT-2026-0114</span></td>
              <td>Tim Sukses Kandidat F<br><span class="small muted">Komite Kandidat F</span></td>
              <td>Yogyakarta</td>
              <td>87</td>
              <td>312</td>
              <td>
                <strong style="color: #16a34a;">100%</strong>
                <div class="compl-bar"><div class="compl-good" style="width: 100%;"></div></div>
              </td>
              <td><span class="small">3–17 Apr 2026</span></td>
              <td><a class="btn ghost small" style="padding-left: 0;">Lihat Trail →</a></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="row" style="margin-top: 16px; align-items: center;">
        <span class="small muted">Menampilkan 6 dari 47 kampanye aktif · Total spend tercatat: Rp 8.4 M</span>
        <div class="right row-tight">
          <button class="btn neutral small">Export CSV</button>
          <button class="btn neutral small">Subscribe Updates</button>
        </div>
      </div>

      <!-- Explainer -->
      <div class="ta-explainer">
        <div class="eyebrow">CARA KERJA</div>
        <h2 style="margin: 8px 0 8px; font-family: var(--font-display); font-size: 26px; letter-spacing: -0.01em;">Bagaimana Audit Trail Bekerja</h2>
        <p class="muted" style="font-size: 15px; max-width: 760px; line-height: 1.7;">
          Setiap aksi di kampanye politik berbayar di Resonansi tercatat di immutable log. Tidak bisa diedit, tidak bisa dihapus — bahkan oleh tim Resonansi sendiri. Berikut yang kami catat dan publikasikan:
        </p>

        <div class="ta-explainer-grid">
          <div class="ta-explain-step">
            <div class="num">1</div>
            <h4 style="margin: 0 0 6px; font-size: 15px;">Brief Publikasi</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">Saat tim sukses publish brief, metadata-nya (sponsor, budget, target audiens, periode) langsung muncul di audit publik.</p>
          </div>
          <div class="ta-explain-step">
            <div class="num">2</div>
            <h4 style="margin: 0 0 6px; font-size: 15px;">Advocate Onboarding</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">Identitas asli setiap advocate (KYC verified) tercatat. Real-name disclosure wajib untuk vertikal politik.</p>
          </div>
          <div class="ta-explain-step">
            <div class="num">3</div>
            <h4 style="margin: 0 0 6px; font-size: 15px;">Konten Publikasi</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">Setiap konten yang diposting wajib include hashtag #KerjasamaResonansi + #IklanPolitik. Sistem auto-attach.</p>
          </div>
          <div class="ta-explain-step">
            <div class="num">4</div>
            <h4 style="margin: 0 0 6px; font-size: 15px;">Real-Time Sync ke Bawaslu</h4>
            <p class="small muted mb-0" style="line-height: 1.6;">Data spend & disclosure di-sync otomatis ke Sekretariat Bawaslu via API. Audit trail publik = data audit Bawaslu.</p>
          </div>
        </div>
      </div>

      <!-- Trust Pillar -->
      <div class="ta-pillar">
        <h3>Setiap aksi di kampanye politik berbayar dicatat dan tidak bisa dihapus.</h3>
        <p style="font-size: 17px; opacity: 0.92; max-width: 700px; margin: 0 auto; line-height: 1.6;">
          Kami percaya demokrasi yang sehat butuh transparansi. Itu sebabnya kami membuka audit trail kampanye politik kepada publik — tanpa pengecualian.
        </p>
        <div class="row-tight" style="margin-top: 24px; justify-content: center;">
          <a class="btn neutral" href="trust.html" style="background: #fff; color: var(--ink);">Baca Trust & Safety</a>
          <a class="btn" href="dispute.html" style="background: #FFB400; color: var(--ink); border-color: #FFB400;">Laporkan Pelanggaran</a>
        </div>
      </div>

      <div style="margin-top: 48px; margin-bottom: 80px;">
        <p class="small muted center">
          Data terakhir di-update 22 April 2026 · 14:30 WIB · Sistem update setiap 5 menit.
        </p>
      </div>
    </div>

    {mega_footer()}
  </div>
</section>'''
    return head + body + chrome_close()


def page_tax_receipt():
    extra = '''<style>
    .tax-hero { padding: 0 0 24px; }
    .tax-tabs { display: flex; gap: 4px; padding: 4px; background: var(--grey-100); border-radius: 12px; margin-bottom: 24px; max-width: fit-content; }
    .tax-tab { padding: 8px 16px; font-size: 13px; font-weight: 500; border-radius: 10px; cursor: pointer; color: var(--muted); }
    .tax-tab.active { background: #fff; color: var(--ink); font-weight: 600; box-shadow: var(--shadow-1); }
    .tax-table { background: #fff; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-1); }
    .tax-table table { width: 100%; border-collapse: collapse; }
    .tax-table th { font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); padding: 14px 20px; text-align: left; border-bottom: 1px solid var(--line); background: var(--grey-50); }
    .tax-table td { padding: 16px 20px; border-bottom: 1px solid var(--grey-100); font-size: 14px; }
    .tax-table tr:last-child td { border-bottom: 0; }
    .tax-table tr:hover { background: var(--grey-50); }
    .tax-table .num { font-family: var(--font-display); font-weight: 600; }
    .tax-total-card { background: linear-gradient(135deg, #0B5FE0 0%, #093F94 100%); color: #fff; border-radius: 16px; padding: 32px; margin-top: 24px; }
    .tax-total-card .num-big { font-family: var(--font-display); font-size: 44px; font-weight: 800; color: #FFB400; line-height: 1; letter-spacing: -0.02em; }
    .tax-total-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 16px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.15); }
    .tax-total-cell .label { font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.7; margin-bottom: 4px; }
    .tax-total-cell .value { font-family: var(--font-display); font-weight: 700; font-size: 20px; }
  </style>'''
    head = chrome('Bukti Potong PPh — Resonansi Advocate', '../', 'advocate/tax-receipt.html', extra)
    body = '''<section class="screen">
  <div class="frame">
    <div class="app-shell">
      <div class="app-sidebar">
        <a class="nav-item" href="../advocate/mobile.html"><svg class="ico" width="18" height="18"><use href="#i-home"/></svg> Home</a>
        <a class="nav-item" href="../advocate/campaigns.html"><svg class="ico" width="18" height="18"><use href="#i-megaphone"/></svg> Kampanye</a>
        <a class="nav-item" href="../advocate/inbox.html"><svg class="ico" width="18" height="18"><use href="#i-mail"/></svg> Inbox</a>
        <a class="nav-item" href="../advocate/profile.html"><svg class="ico" width="18" height="18"><use href="#i-user"/></svg> Profile</a>
        <a class="nav-item" href="../advocate/verification.html"><svg class="ico" width="18" height="18"><use href="#i-shield"/></svg> Verification</a>
        <a class="nav-item active" href="../advocate/tax-receipt.html"><svg class="ico" width="18" height="18"><use href="#i-card"/></svg> Bukti PPh</a>
      </div>

      <div class="app-main">
        <div class="row" style="margin-bottom: 8px;">
          <div>
            <h1 style="margin: 0; font-size: 28px; letter-spacing: -0.02em;">Bukti Potong PPh</h1>
            <p class="muted small mb-0" style="margin-top: 4px;">Dokumen pajak untuk pelaporan SPT Tahunan Anda.</p>
          </div>
          <div class="right row-tight">
            <button class="btn neutral">📅 Periode Custom</button>
            <button class="btn">Download Semua (PDF)</button>
          </div>
        </div>

        <!-- Tax tabs -->
        <div class="tax-tabs" style="margin-top: 16px;">
          <div class="tax-tab">2024</div>
          <div class="tax-tab">2025</div>
          <div class="tax-tab active">2026</div>
        </div>

        <p class="small muted" style="margin-top: 8px;">Periode pelaporan: Januari – April 2026 · NPWP: 12.345.678.9-012.000</p>

        <!-- Per-month table -->
        <div class="tax-table" style="margin-top: 8px;">
          <table>
            <thead>
              <tr>
                <th>Bulan</th>
                <th>Total Earning (Bruto)</th>
                <th>PPh 21 (5%)</th>
                <th>PPh 23 (2%)</th>
                <th>Total Dipotong</th>
                <th>Diterima (Netto)</th>
                <th>Bukti Potong</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>April 2026</strong><br><span class="small muted">12 kampanye selesai</span></td>
                <td class="num">Rp 8.450.000</td>
                <td class="num">Rp 422.500</td>
                <td class="num">Rp 169.000</td>
                <td class="num" style="color:#d4404a;">Rp 591.500</td>
                <td class="num" style="color:#16a34a;">Rp 7.858.500</td>
                <td><a class="btn ghost small" style="padding-left: 0;">⬇ Download PDF</a></td>
              </tr>
              <tr>
                <td><strong>Maret 2026</strong><br><span class="small muted">8 kampanye selesai</span></td>
                <td class="num">Rp 6.200.000</td>
                <td class="num">Rp 310.000</td>
                <td class="num">Rp 124.000</td>
                <td class="num" style="color:#d4404a;">Rp 434.000</td>
                <td class="num" style="color:#16a34a;">Rp 5.766.000</td>
                <td><a class="btn ghost small" style="padding-left: 0;">⬇ Download PDF</a></td>
              </tr>
              <tr>
                <td><strong>Februari 2026</strong><br><span class="small muted">6 kampanye selesai</span></td>
                <td class="num">Rp 4.800.000</td>
                <td class="num">Rp 240.000</td>
                <td class="num">Rp 96.000</td>
                <td class="num" style="color:#d4404a;">Rp 336.000</td>
                <td class="num" style="color:#16a34a;">Rp 4.464.000</td>
                <td><a class="btn ghost small" style="padding-left: 0;">⬇ Download PDF</a></td>
              </tr>
              <tr>
                <td><strong>Januari 2026</strong><br><span class="small muted">10 kampanye selesai</span></td>
                <td class="num">Rp 7.300.000</td>
                <td class="num">Rp 365.000</td>
                <td class="num">Rp 146.000</td>
                <td class="num" style="color:#d4404a;">Rp 511.000</td>
                <td class="num" style="color:#16a34a;">Rp 6.789.000</td>
                <td><a class="btn ghost small" style="padding-left: 0;">⬇ Download PDF</a></td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Total -->
        <div class="tax-total-card">
          <div style="display:flex; justify-content:space-between; align-items:flex-end;">
            <div>
              <div style="font-size: 13px; opacity: 0.8; text-transform: uppercase; letter-spacing: 0.05em;">Total Earning 2026 YTD</div>
              <div class="num-big" style="margin-top: 4px;">Rp 26.750.000</div>
            </div>
            <a href="#" class="btn" style="background: #FFB400; color: var(--ink); border-color: #FFB400;">Download SPT Tahunan Helper →</a>
          </div>

          <div class="tax-total-grid">
            <div class="tax-total-cell">
              <div class="label">Total PPh Dipotong</div>
              <div class="value">Rp 1.872.500</div>
            </div>
            <div class="tax-total-cell">
              <div class="label">Total Diterima (Netto)</div>
              <div class="value">Rp 24.877.500</div>
            </div>
            <div class="tax-total-cell">
              <div class="label">Total Kampanye Selesai</div>
              <div class="value">36 kampanye</div>
            </div>
          </div>
        </div>

        <div style="margin-top: 24px; padding: 20px 24px; background: var(--accent-soft); border-radius: 12px; display: flex; gap: 16px; align-items: flex-start;">
          <svg width="24" height="24" style="color: var(--accent); flex-shrink: 0; margin-top: 2px;"><use href="#i-shield"/></svg>
          <div>
            <strong>Cara menggunakan bukti potong ini</strong>
            <p class="small muted mb-0" style="margin-top: 6px; line-height: 1.6;">
              Bukti potong PPh ini sudah otomatis ter-sync ke DJP Online dengan NPWP Anda. Anda tidak perlu input manual — cukup login ke <strong>djponline.pajak.go.id</strong>, semua data sudah ada di pre-filled SPT Tahunan. Resonansi sebagai pemotong sudah lapor SPT Masa setiap bulan.
            </p>
            <div class="row-tight" style="margin-top: 10px;">
              <a class="btn ghost small" style="padding-left: 0;" href="../faq.html">FAQ Perpajakan →</a>
              <a class="btn ghost small" style="padding-left: 0;" href="../contact.html">Tanya konsultan pajak →</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>'''
    return head + body + chrome_close()


def page_welcome():
    extra = '''<style>
    body { background: linear-gradient(180deg, #f5f6f8 0%, #fff 100%); }
    .welcome-wrap { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px 24px; }
    .welcome-progress { max-width: 760px; width: 100%; margin-bottom: 24px; }
    .welcome-progress-bar { display: flex; gap: 6px; margin-bottom: 12px; }
    .welcome-progress-bar > div { flex: 1; height: 6px; background: var(--grey-200); border-radius: 3px; transition: background 0.3s; }
    .welcome-progress-bar > div.done { background: var(--accent); }
    .welcome-progress-bar > div.active { background: var(--accent); position: relative; overflow: hidden; }
    .welcome-progress-bar > div.active::after { content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent); animation: shimmer 1.6s infinite; }
    @keyframes shimmer { from { transform: translateX(-100%); } to { transform: translateX(100%); } }
    .welcome-step-label { display: flex; justify-content: space-between; align-items: center; font-size: 12.5px; color: var(--muted); }
    .welcome-step-label strong { color: var(--ink); }
    .welcome-cards { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; max-width: 760px; width: 100%; }
    .wc { background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 32px 28px; box-shadow: var(--shadow-1); position: relative; }
    .wc.done { border-color: #b4d8c0; }
    .wc.done::after { content: "✓"; position: absolute; top: 16px; right: 16px; width: 28px; height: 28px; border-radius: 50%; background: #16a34a; color: #fff; font-weight: 700; display: flex; align-items: center; justify-content: center; }
    .wc.active { border-color: var(--accent); box-shadow: 0 8px 28px rgba(11,95,224,0.16); }
    .wc .step-num { display: inline-flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: var(--accent-soft); color: var(--accent); font-family: var(--font-display); font-weight: 800; font-size: 15px; margin-bottom: 16px; }
    .wc.active .step-num { background: var(--accent); color: #fff; }
    .wc.done .step-num { background: #16a34a; color: #fff; }
    .wc h3 { font-family: var(--font-display); font-size: 20px; margin: 0 0 8px; letter-spacing: -0.01em; }
    .wc p { color: var(--muted); font-size: 14.5px; line-height: 1.6; margin: 0 0 18px; }
    .skip-link { margin-top: 24px; text-align: center; }
    .skip-link a { color: var(--muted); text-decoration: none; font-size: 13.5px; }
    .skip-link a:hover { color: var(--accent); }
  </style>'''
    head = chrome('Selamat Datang — Resonansi', '', 'welcome.html', extra)
    body = '''<div class="welcome-wrap">

  <a class="logo" href="index.html" style="margin-bottom: 24px;">RESONANSI</a>

  <!-- Progress -->
  <div class="welcome-progress">
    <div class="welcome-step-label">
      <span><strong>Setup akun</strong> · 4 dari 5 selesai</span>
      <span>Step 1 dari 4</span>
    </div>
    <div class="welcome-progress-bar" style="margin-top: 8px;">
      <div class="done"></div>
      <div class="done"></div>
      <div class="done"></div>
      <div class="done"></div>
      <div class="active"></div>
    </div>
  </div>

  <h1 style="margin: 0 0 8px; font-size: 36px; letter-spacing: -0.025em; text-align: center;">Selamat datang di Resonansi 👋</h1>
  <p class="muted" style="font-size: 16px; max-width: 640px; text-align: center; margin: 0 0 36px;">
    Akun Anda sudah siap. Mari mulai dengan 4 langkah cepat untuk meluncurkan kampanye pertama Anda.
  </p>

  <!-- 4 Cards -->
  <div class="welcome-cards">
    <div class="wc active">
      <div class="step-num">1</div>
      <h3>Mengenal Dashboard</h3>
      <p>Tour 90 detik ke fitur utama Resonansi — brief builder, kampanye, advocate library, analytics, dan billing.</p>
      <button class="btn">Mulai Tour →</button>
    </div>
    <div class="wc">
      <div class="step-num">2</div>
      <h3>Buat Brief Pertama</h3>
      <p>Wizard 5 langkah: tujuan, target audiens, deliverables, budget, dan timeline. Hanya 8 menit.</p>
      <a href="client/brief.html" class="btn neutral">Buat Brief →</a>
    </div>
    <div class="wc">
      <div class="step-num">3</div>
      <h3>Pelajari Analytics</h3>
      <p>Lihat sentiment real-time, sentiment per region, ROI calculator, dan compare campaign performance.</p>
      <a href="client/analytics.html" class="btn neutral">Buka Analytics →</a>
    </div>
    <div class="wc">
      <div class="step-num">4</div>
      <h3>Siap Meluncur</h3>
      <p>Setelah brief publish, advocate akan apply dalam 24 jam. Tim Resonansi membantu shortlist 7 advocate terbaik.</p>
      <a href="client/dashboard.html" class="btn neutral">Ke Dashboard →</a>
    </div>
  </div>

  <div class="skip-link">
    <a href="client/dashboard.html">Skip tour, lanjut ke Dashboard →</a>
  </div>

  <p class="small muted" style="margin-top: 48px; max-width: 600px; text-align: center; line-height: 1.6;">
    💡 Butuh bantuan? Customer Success kami online 24/7 di chat (icon kanan bawah dashboard) atau email <a href="contact.html" style="color: var(--accent);">success@resonansi.id</a>.
  </p>
</div>'''
    return head + body + chrome_close()


def page_notifications():
    extra = '''<style>
    .notif-tabs { display: flex; gap: 4px; padding: 4px; background: var(--grey-100); border-radius: 12px; max-width: fit-content; margin-bottom: 20px; }
    .notif-tab { padding: 8px 14px; font-size: 13px; font-weight: 500; border-radius: 10px; cursor: pointer; color: var(--muted); display: inline-flex; align-items: center; gap: 6px; }
    .notif-tab.active { background: #fff; color: var(--ink); font-weight: 600; box-shadow: var(--shadow-1); }
    .notif-tab .badge { display: inline-flex; align-items: center; justify-content: center; min-width: 18px; height: 18px; padding: 0 5px; border-radius: 9px; background: var(--accent); color: #fff; font-size: 10.5px; font-weight: 700; }
    .notif-list { background: #fff; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; box-shadow: var(--shadow-1); }
    .notif-item { display: grid; grid-template-columns: 44px 1fr auto auto; gap: 16px; padding: 18px 20px; border-bottom: 1px solid var(--grey-100); align-items: flex-start; transition: background 0.15s; cursor: pointer; }
    .notif-item:last-child { border: 0; }
    .notif-item:hover { background: var(--grey-50); }
    .notif-item.unread { background: var(--accent-soft); }
    .notif-item.unread:hover { background: #d8e4f9; }
    .notif-item .ico-wrap { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .notif-item .ico-wrap.action { background: #fff4d6; color: #b88300; }
    .notif-item .ico-wrap.update { background: var(--accent-soft); color: var(--accent); }
    .notif-item .ico-wrap.payment { background: #d8f0e3; color: #0a6a3a; }
    .notif-item .ico-wrap.dispute { background: var(--danger-soft); color: #9c1c1c; }
    .notif-item .ico-wrap.system { background: var(--grey-100); color: var(--grey-700); }
    .notif-item .title { font-weight: 600; font-size: 14px; color: var(--ink); margin-bottom: 4px; }
    .notif-item .body { font-size: 13px; color: var(--muted); line-height: 1.55; }
    .notif-item .time { font-size: 12px; color: var(--muted); white-space: nowrap; margin-top: 4px; }
    .notif-item.unread::before { content: ""; display: block; width: 8px; height: 8px; background: var(--accent); border-radius: 50%; position: absolute; left: 6px; top: 28px; }
    .notif-item { position: relative; padding-left: 28px; }
  </style>'''
    head = chrome('Notifikasi — Resonansi', '', 'notifications.html', extra)
    body = '''<section class="screen">
  <div class="frame">
    <div class="app-shell">
      <div class="app-sidebar">
        <a class="nav-item" href="client/dashboard.html"><svg class="ico" width="18" height="18"><use href="#i-home"/></svg> Home</a>
        <a class="nav-item" href="client/brief.html"><svg class="ico" width="18" height="18"><use href="#i-edit"/></svg> Buat Brief</a>
        <a class="nav-item" href="client/campaigns.html"><svg class="ico" width="18" height="18"><use href="#i-megaphone"/></svg> Kampanye</a>
        <a class="nav-item" href="client/library.html"><svg class="ico" width="18" height="18"><use href="#i-bookmark"/></svg> Advocate Library</a>
        <a class="nav-item" href="client/analytics.html"><svg class="ico" width="18" height="18"><use href="#i-chart"/></svg> Analytics</a>
        <a class="nav-item" href="client/billing.html"><svg class="ico" width="18" height="18"><use href="#i-card"/></svg> Billing</a>
        <a class="nav-item active" href="notifications.html"><svg class="ico" width="18" height="18"><use href="#i-bell"/></svg> Notifikasi</a>
        <a class="nav-item" href="client/settings.html"><svg class="ico" width="18" height="18"><use href="#i-settings"/></svg> Settings</a>
      </div>

      <div class="app-main">
        <div class="row" style="align-items: flex-start;">
          <div>
            <h1 style="margin: 0; font-size: 28px; letter-spacing: -0.02em;">Notifikasi</h1>
            <p class="muted small mb-0" style="margin-top: 4px;">8 baru · 3 perlu aksi · update terakhir 2 menit lalu</p>
          </div>
          <div class="right row-tight">
            <button class="btn neutral">Mark all as read</button>
            <button class="btn neutral">⚙ Pengaturan Notifikasi</button>
          </div>
        </div>

        <!-- Tabs -->
        <div class="notif-tabs" style="margin-top: 20px;">
          <div class="notif-tab active">Semua <span class="badge">8</span></div>
          <div class="notif-tab">Aksi Diperlukan <span class="badge">3</span></div>
          <div class="notif-tab">Update Kampanye</div>
          <div class="notif-tab">Sistem</div>
        </div>

        <!-- List -->
        <div class="notif-list">

          <div class="notif-item unread">
            <div class="ico-wrap action">
              <svg width="20" height="20"><use href="#i-edit"/></svg>
            </div>
            <div>
              <div class="title">4 konten baru menunggu approval</div>
              <div class="body">Kampanye Film X — Opening Weekend. Tenggat tinggal <strong>6 jam</strong> sebelum konten dijadwalkan live.</div>
            </div>
            <div class="time">2 menit lalu</div>
            <a href="client/approval.html" class="btn small">Review →</a>
          </div>

          <div class="notif-item unread">
            <div class="ico-wrap dispute">
              <svg width="20" height="20"><use href="#i-shield"/></svg>
            </div>
            <div>
              <div class="title">⚠ 1 advocate gagal verifikasi proof-of-work</div>
              <div class="body"><strong>@advocate_xy</strong> di Film Y. Pembayaran ditahan, perlu keputusan Anda dalam 48 jam.</div>
            </div>
            <div class="time">14 menit lalu</div>
            <a href="dispute.html" class="btn small" style="background: #d4404a; border-color: #d4404a;">Tinjau Sengketa →</a>
          </div>

          <div class="notif-item unread">
            <div class="ico-wrap payment">
              <svg width="20" height="20"><use href="#i-wallet"/></svg>
            </div>
            <div>
              <div class="title">💰 Pembayaran diterima — Rp 480 jt</div>
              <div class="body">Top-up saldo escrow untuk kampanye Film Z berhasil. Saldo aktif sekarang Rp 720 jt.</div>
            </div>
            <div class="time">1 jam lalu</div>
            <a href="client/billing.html" class="btn ghost small">Lihat →</a>
          </div>

          <div class="notif-item unread">
            <div class="ico-wrap update">
              <svg width="20" height="20"><use href="#i-chart"/></svg>
            </div>
            <div>
              <div class="title">📈 Sentiment alert: Film X Jateng</div>
              <div class="body">Sentiment +0.84 di Yogya, peak performance terbaik dari semua region. Pertimbangkan re-allocate budget Rp 40 jt ke region ini.</div>
            </div>
            <div class="time">3 jam lalu</div>
            <a href="client/analytics.html" class="btn ghost small">Analytics →</a>
          </div>

          <div class="notif-item unread">
            <div class="ico-wrap update">
              <svg width="20" height="20"><use href="#i-users"/></svg>
            </div>
            <div>
              <div class="title">12 advocate baru bergabung ke library Anda</div>
              <div class="body">Library "Film Drama Lovers" diperbarui — total sekarang 247 advocate. Match score rata-rata 78%.</div>
            </div>
            <div class="time">5 jam lalu</div>
            <a href="client/library.html" class="btn ghost small">Lihat →</a>
          </div>

          <div class="notif-item">
            <div class="ico-wrap update">
              <svg width="20" height="20"><use href="#i-megaphone"/></svg>
            </div>
            <div>
              <div class="title">Kampanye Film Y mencapai 5M reach</div>
              <div class="body">Milestone tercapai! 620 advocate sudah aktif. Estimasi reach final: 8–10M.</div>
            </div>
            <div class="time">Kemarin</div>
            <a href="client/live-campaign.html" class="btn ghost small">Lihat →</a>
          </div>

          <div class="notif-item">
            <div class="ico-wrap system">
              <svg width="20" height="20"><use href="#i-zap"/></svg>
            </div>
            <div>
              <div class="title">✨ Fitur baru: Trust Audit Publik</div>
              <div class="body">Sekarang Anda bisa lihat audit trail publik untuk semua kampanye politik di Resonansi. Compliance Bawaslu transparant.</div>
            </div>
            <div class="time">2 hari lalu</div>
            <a href="trust-audit.html" class="btn ghost small">Coba →</a>
          </div>

          <div class="notif-item">
            <div class="ico-wrap system">
              <svg width="20" height="20"><use href="#i-mail"/></svg>
            </div>
            <div>
              <div class="title">Invoice INV-2026-0418 sudah tersedia</div>
              <div class="body">Total Rp 240 jt untuk kampanye Film Y. Auto-debit dari kartu kredit tertaut pada 25 April 2026.</div>
            </div>
            <div class="time">3 hari lalu</div>
            <a href="client/billing.html" class="btn ghost small">Lihat →</a>
          </div>

        </div>

        <div style="margin-top: 20px; padding: 20px 24px; background: var(--grey-50); border-radius: 12px; display: flex; align-items: center; gap: 16px;">
          <svg width="22" height="22" style="color: var(--muted);"><use href="#i-settings"/></svg>
          <div style="flex:1;">
            <strong style="font-size: 14px;">Pengaturan Notifikasi</strong>
            <div class="small muted" style="margin-top: 2px;">Atur frekuensi email + push notification per kategori.</div>
          </div>
          <a href="client/settings.html" class="btn neutral small">Buka Settings →</a>
        </div>

        <p class="small muted center" style="margin-top: 24px;">
          Lihat notifikasi lebih lama dari 30 hari di <a href="#" style="color: var(--accent);">arsip</a>.
        </p>

      </div>
    </div>
  </div>
</section>'''
    return head + body + chrome_close()


def main():
    pages = [
        ('trust-audit.html', page_trust_audit),
        ('advocate/tax-receipt.html', page_tax_receipt),
        ('welcome.html', page_welcome),
        ('notifications.html', page_notifications),
    ]
    for rel, fn in pages:
        write_page(rel, fn())
    print(f'\n  → wrote {len(pages)} pages (batch 3)')


if __name__ == '__main__':
    main()
