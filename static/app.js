document.addEventListener('DOMContentLoaded', function () {

  // ── Therapy form ──
  const therapyForm = document.getElementById('therapy-form');
  if (therapyForm) {
    const classMap = { check: 'sel-check', partial: 'sel-partial', cross: 'sel-cross' };

    therapyForm.querySelectorAll('.try-btn').forEach(btn => {
      btn.addEventListener('click', function () {
        const group = this.dataset.group;
        const val   = this.dataset.val;
        therapyForm.querySelector(`input[name="t${group}"]`).value = val;
        therapyForm.querySelectorAll(`.try-btn[data-group="${group}"]`).forEach(b => {
          b.className = 'try-btn';
        });
        this.classList.add(classMap[val]);
      });
    });

    const moodInput = document.getElementById('mood-input');
    if (moodInput) {
      therapyForm.querySelectorAll('.mood-btn').forEach(btn => {
        btn.addEventListener('click', function () {
          therapyForm.querySelectorAll('.mood-btn').forEach(b => b.classList.remove('selected'));
          this.classList.add('selected');
          moodInput.value = this.dataset.val;
        });
      });
    }

    therapyForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const tries = [];
      for (let i = 0; i < 5; i++) {
        tries.push(therapyForm.querySelector(`input[name="t${i}"]`).value);
      }
      const mood = moodInput ? moodInput.value : 'happy';
      fetch('/therapy/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tries, mood })
      }).then(r => r.json()).then(() => {
        window.location.href = '/therapy/result';
      });
    });
  }

  // ── Milestone form ──
  const msForm = document.getElementById('ms-form');
  if (msForm) {
    const msClassMap = { check: 'sel-check', partial: 'sel-partial', cross: 'sel-cross' };

    msForm.querySelectorAll('.ms-opt').forEach(btn => {
      btn.addEventListener('click', function () {
        const ms  = this.dataset.ms;
        const val = this.dataset.val;
        msForm.querySelector(`input[name="ms_${ms}"]`).value = val;
        this.closest('.ms-btns').querySelectorAll('.ms-opt').forEach(b => {
          b.className = 'ms-opt';
        });
        this.classList.add(msClassMap[val]);
      });
    });

    msForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const data = {};
      ['ms1','ms2','ms3','ms4','ms5','ms6','ms7','ms8'].forEach(k => {
        data[k] = msForm.querySelector(`input[name="ms_${k}"]`).value;
      });

      fetch('/milestone/result', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      }).then(r => r.json()).then(res => {
        const verdict =
          res.pct >= 70 ? ['✅ Perkembangan Baik', 'Pencapaian Ahmad berada dalam julat yang baik. Teruskan sokongan semasa.', 'success']
          : res.pct >= 40 ? ['⚠️ Perlu Perhatian', 'Beberapa kawasan memerlukan sokongan tambahan. Rujuk rancangan intervensi.', 'warn']
          : ['🚨 Intervensi Segera', 'Skor rendah menunjukkan keperluan intervensi segera. Hantar rujukan ke hospital.', 'danger'];

        const sPct = Math.round(res.social / 8 * 100);
        const cPct = Math.round(res.comm   / 8 * 100);

        const actionBtn = verdict[2] === 'danger'
          ? `<a href="#" class="btn btn-danger btn-full" onclick="alert('Laporan dihantar ke Hospital Sultanah Aminah. No. Rujukan: HSA-20260519-0089');return false;">🚨 &nbsp; Hantar Rujukan Segera ke Hospital</a>`
          : `<a href="#" class="btn btn-primary btn-full" onclick="alert('Laporan dihantar ke pakar untuk semakan.');return false;">📨 &nbsp; Hantar ke Pakar untuk Semakan</a>`;

        document.getElementById('report-panel').innerHTML = `
          <div class="result-hero">
            <div class="result-hero-label">Keputusan Penilaian</div>
            <div class="result-hero-name">Ahmad bin Hassan &nbsp;·&nbsp; 4 tahun</div>
            <div class="result-hero-meta">Fadzli bin Nordin &nbsp;·&nbsp; 19 Mei 2026</div>
            <div class="result-hero-pct">${res.pct}%</div>
            <div class="result-hero-score">${res.total} daripada ${res.max} markah</div>
          </div>
          <div class="alert alert-${verdict[2]}">
            <div class="alert-title">${verdict[0]}</div>
            <div class="alert-body">${verdict[1]}</div>
          </div>
          <div class="section-label">Pecahan Mengikut Kategori</div>
          <div class="card">
            <div style="padding:8px 0;">
              <div class="score-wrap">
                <div class="score-label-row"><span>Sosial</span><span>${res.social} / 8</span></div>
                <div class="score-track"><div class="score-fill" style="width:${sPct}%;"></div></div>
              </div>
              <div class="score-wrap" style="margin-bottom:4px;">
                <div class="score-label-row"><span>Komunikasi</span><span>${res.comm} / 8</span></div>
                <div class="score-track"><div class="score-fill" style="width:${cPct}%;"></div></div>
              </div>
            </div>
          </div>
          ${actionBtn}
          <a href="/milestone" class="btn btn-secondary btn-full">🔄 &nbsp; Mulakan Penilaian Baru</a>
        `;
        document.getElementById('report-panel').style.display = 'block';
        document.getElementById('ms-form-wrap').style.display = 'none';
      });
    });
  }

  // ── Referral form ──
  const refSubmit = document.getElementById('ref-submit');
  if (refSubmit) {
    refSubmit.addEventListener('click', function () {
      document.getElementById('ref-form').style.display    = 'none';
      document.getElementById('ref-success').style.display = 'block';
    });
  }

});
