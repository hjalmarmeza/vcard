import sys

with open('/Users/hjalmarmeza/Downloads/Antigravity/CV/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to insert a glowing QR code or CTA before the footer.
target_str = "            {/* FOOTER */}"
qr_code_html = """
            {/* CALL TO ACTION DIGITAL - IMPACTO VISUAL FINAL */}
            <section className="p-8 md:p-16 border-t border-slate-800/50 bg-gradient-to-br from-[#0a1120] to-[#040812] relative z-20 flex flex-col md:flex-row items-center justify-between gap-10">
              <div className="absolute inset-0 bg-amber-500/5 opacity-50 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-amber-500/10 via-transparent to-transparent"></div>
              
              <div className="relative z-10 flex-1 text-center md:text-left">
                <h3 className="text-[10px] md:text-xs font-black text-amber-500 uppercase tracking-[0.3em] mb-3">
                  <i className="fas fa-satellite-dish mr-2 animate-pulse"></i> Sincronización Directa
                </h3>
                <h2 className="text-3xl md:text-5xl font-black text-white uppercase tracking-tighter mb-4">
                  Inicia la <span className="text-amber-500">Transformación</span>
                </h2>
                <p className="text-slate-400 text-sm md:text-base max-w-xl leading-relaxed font-medium mb-6">
                  Mi enfoque no es la tecnología por sí misma, sino la rentabilidad operativa. 
                  Si tu organización necesita escalar de forma autónoma, reducir costos o modernizar su capa de gestión, hablemos de soluciones tangibles hoy mismo.
                </p>
                <div className="flex flex-wrap gap-4 justify-center md:justify-start">
                  <a href="https://linkedin.com/in/hjalmarmeza" target="_blank" rel="noreferrer" className="px-6 py-3 bg-amber-500 hover:bg-amber-400 text-slate-900 font-black uppercase text-xs md:text-sm tracking-widest rounded-full transition-all duration-300 shadow-[0_0_20px_rgba(245,158,11,0.3)] hover:shadow-[0_0_30px_rgba(245,158,11,0.5)] hover:-translate-y-1 flex items-center gap-2">
                    <i className="fab fa-linkedin-in text-lg"></i> Conectar en LinkedIn
                  </a>
                  <a href="mailto:hmeza.cortez@gmail.com" className="px-6 py-3 bg-[#1e293b] border border-slate-700 hover:border-amber-500/50 text-white font-bold uppercase text-xs md:text-sm tracking-widest rounded-full transition-all duration-300 hover:bg-slate-800 flex items-center gap-2">
                    <i className="fas fa-envelope text-lg text-amber-500"></i> Agendar Call
                  </a>
                </div>
              </div>

              {/* QR Code / Digital Card visual */}
              <div className="relative z-10 w-full md:w-auto flex justify-center perspective-[1000px]">
                <div className="relative w-48 h-48 md:w-64 md:h-64 bg-slate-900/80 rounded-3xl border border-slate-700 p-2 shadow-[0_20px_50px_rgba(0,0,0,0.5)] transform rotate-y-[-5deg] rotate-x-[5deg] hover:rotate-y-0 hover:rotate-x-0 transition-all duration-700 group">
                  <div className="absolute inset-0 bg-gradient-to-tr from-amber-500/20 to-transparent rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-700 blur"></div>
                  <div className="w-full h-full bg-[#0a1120] rounded-2xl border border-slate-800 flex flex-col items-center justify-center p-6 relative overflow-hidden">
                    {/* Fake scanning line */}
                    <div className="absolute top-0 left-0 right-0 h-1 bg-amber-500 shadow-[0_0_15px_#f59e0b] animate-[scan_3s_ease-in-out_infinite]"></div>
                    <style dangerouslySetInnerHTML={{__html: `
                      @keyframes scan {
                        0%, 100% { top: 0; opacity: 0; }
                        50% { top: 100%; opacity: 1; }
                      }
                    `}} />
                    
                    <i className="fas fa-qrcode text-6xl md:text-8xl text-slate-400 group-hover:text-amber-500 transition-colors duration-500 mb-4"></i>
                    <div className="text-[9px] font-black uppercase tracking-[0.2em] text-center text-slate-300 flex flex-col gap-1">
                      <span>Escanea o Clickea</span>
                      <span className="text-amber-500">Para contacto directo</span>
                    </div>
                  </div>
                </div>
              </div>
            </section>

"""

if target_str in content:
    content = content.replace(target_str, qr_code_html + "\n" + target_str)
    with open('/Users/hjalmarmeza/Downloads/Antigravity/CV/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Success")
else:
    print("Target string not found")
