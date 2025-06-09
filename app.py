from pathlib import Path

# Conteúdo do HTML salvo anteriormente no canvas
html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simulador de Satisfação - MMX Okiar</title>
  <style>
    body {
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f5f5f5;
      margin: 0;
      padding: 20px;
      color: #333;
    }
    .container {
      display: flex;
      justify-content: space-between;
      gap: 20px;
    }
    .card, .center-card {
      background: white;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      padding: 20px;
      flex: 1;
    }
    .center-card {
      background: #c62828;
      color: white;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    .slider-group {
      margin-bottom: 30px;
    }
    input[type=range] {
      width: 100%;
    }
    .delta {
      font-weight: bold;
    }
    .green { color: green; }
    .red { color: red; }
  </style>
</head>
<body>
  <h1>Simulador de Satisfação - MMX Okiar</h1>
  <div class="container">
    <div>
      <div class="card slider-group">
        <label>Segurança: <span id="delta_seguranca" class="delta">+0.0%</span></label>
        <input type="range" min="0" max="10" step="0.1" value="6" id="seguranca">
      </div>
      <div class="card slider-group">
        <label>Responsividade: <span id="delta_responsividade" class="delta">+0.0%</span></label>
        <input type="range" min="0" max="10" step="0.1" value="6" id="responsividade">
      </div>
      <div class="card slider-group">
        <label>Tangível: <span id="delta_tangivel" class="delta">+0.0%</span></label>
        <input type="range" min="0" max="10" step="0.1" value="6" id="tangivel">
      </div>
      <div class="card slider-group">
        <label>Confiabilidade: <span id="delta_confiabilidade" class="delta">+0.0%</span></label>
        <input type="range" min="0" max="10" step="0.1" value="6" id="confiabilidade">
      </div>
      <div class="card slider-group">
        <label>Empatia: <span id="delta_empatia" class="delta">+0.0%</span></label>
        <input type="range" min="0" max="10" step="0.1" value="6" id="empatia">
      </div>
    </div>
    <div class="center-card">
      <h2>Satisfação</h2>
      <div id="satisfacao_val" style="font-size: 48px;">6.0</div>
      <div id="satisfacao_delta" class="delta">+0.0%</div>
    </div>
    <div>
      <div class="card">
        <strong>Recompra</strong>
        <div id="recompra_val">8.1</div>
        <div id="delta_recompra" class="delta">+0.0%</div>
      </div>
      <div class="card">
        <strong>Intenção de Pagar Mais</strong>
        <div id="intencao_pagar_val">7.2</div>
        <div id="delta_intencao_pagar" class="delta">+0.0%</div>
      </div>
      <div class="card">
        <strong>Intenção de Recomendar</strong>
        <div id="intencao_recomendar_val">7.8</div>
        <div id="delta_intencao_recomendar" class="delta">+0.0%</div>
      </div>
      <div class="card">
        <strong>Força de Marca</strong>
        <div id="forca_marca_val">6.9</div>
        <div id="delta_forca_marca" class="delta">+0.0%</div>
      </div>
    </div>
  </div>
<script>
  const refValues = {
    seguranca: 6,
    responsividade: 6,
    tangivel: 6,
    confiabilidade: 6,
    empatia: 6
  };

  function update() {
    const v = Object.fromEntries(Object.keys(refValues).map(k => [k, parseFloat(document.getElementById(k).value)]));
    for (let k in v) {
      const change = ((v[k] - refValues[k]) / refValues[k]) * 100;
      const el = document.getElementById(`delta_${k}`);
      el.textContent = `${change >= 0 ? '+' : ''}${change.toFixed(1)}%`;
      el.className = `delta ${change > 0 ? 'green' : change < 0 ? 'red' : ''}`;
    }

    const satisfacao = 0.25 * v.seguranca + 0.2 * v.responsividade + 0.15 * v.tangivel + 0.3 * v.confiabilidade + 0.1 * v.empatia;
    const refSatisfacao = 6;
    const changeS = ((satisfacao - refSatisfacao) / refSatisfacao) * 100;
    document.getElementById("satisfacao_val").textContent = satisfacao.toFixed(1);
    document.getElementById("satisfacao_delta").textContent = `${changeS >= 0 ? '+' : ''}${changeS.toFixed(1)}%`;
    document.getElementById("satisfacao_delta").className = `delta ${changeS > 0 ? 'green' : changeS < 0 ? 'red' : ''}`;

    const results = {
      recompra: satisfacao * 0.35 + 6.0,
      intencao_pagar: satisfacao * 0.2 + 6.0,
      intencao_recomendar: satisfacao * 0.3 + 6.0,
      forca_marca: satisfacao * 0.15 + 6.0
    };
    const refS = 6.0;
    const ref = {
      recompra: refS * 0.35 + 6.0,
      intencao_pagar: refS * 0.2 + 6.0,
      intencao_recomendar: refS * 0.3 + 6.0,
      forca_marca: refS * 0.15 + 6.0
    };

    for (let k in results) {
      document.getElementById(`${k}_val`).textContent = results[k].toFixed(1);
      const delta = ((results[k] - ref[k]) / ref[k]) * 100;
      const el = document.getElementById(`delta_${k}`);
      el.textContent = `${delta >= 0 ? '+' : ''}${delta.toFixed(1)}%`;
      el.className = `delta ${delta > 0 ? 'green' : delta < 0 ? 'red' : ''}`;
    }
  }

  document.querySelectorAll("input[type=range]").forEach(el => el.addEventListener("input", update));
  update();
</script>
</body>
</html>
"""

file_path = "/mnt/data/simulador_mmx.html"
Path(file_path).write_text(html_content, encoding="utf-8")
file_path
