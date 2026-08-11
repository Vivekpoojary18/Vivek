import zlib

def create_resume_pdf(filename="Vivek_J_Poojary_Resume.pdf"):
    # PDF generation using PostScript commands in PDF stream
    stream_content = """
/Helvetica-Bold findfont 22 scalefont setfont
40 750 moveto
(VIVEK J POOJARY) show

/Helvetica findfont 9 scalefont setfont
40 735 moveto
(Mangaluru, Karnataka, India | vivekjpoojary@gmail.com | +91 82173 67683 | github.com/vivekjpoojary) show

0.8 0.8 0.8 setrgbcolor
40 725 moveto 555 725 lineto stroke
0 setrgbcolor

/Helvetica-Bold findfont 11 scalefont setfont
40 708 moveto
(SUMMARY) show

/Helvetica findfont 9 scalefont setfont
40 694 moveto
(Builds and ships systems that turn raw data into decisions -- from a retrieval-augmented AI platform serving) show
40 682 moveto
(page-accurate answers across documents to a demand-forecasting engine shaping real-time resource allocation.) show
40 670 moveto
(IBM-certified Data Science practitioner (BCA, CGPA 8.08) seeking Data Analyst / Data Science / AI-ML roles.) show

0.8 0.8 0.8 setrgbcolor
40 658 moveto 555 658 lineto stroke
0 setrgbcolor

/Helvetica-Bold findfont 11 scalefont setfont
40 641 moveto
(EDUCATION) show

/Helvetica-Bold findfont 9.5 scalefont setfont
40 627 moveto
(Bachelor of Computer Applications (BCA)) show
/Helvetica findfont 9 scalefont setfont
240 627 moveto
(Jun 2023 - May 2026) show
40 615 moveto
(St. Aloysius (Deemed to be University), Mangaluru, Karnataka) show
40 603 moveto
(CGPA: 8.08 / 10.0 | Class Representative (2024-25)) show

0.8 0.8 0.8 setrgbcolor
40 591 moveto 555 591 lineto stroke
0 setrgbcolor

/Helvetica-Bold findfont 11 scalefont setfont
40 574 moveto
(TECHNICAL SKILLS) show

/Helvetica findfont 9 scalefont setfont
40 560 moveto
(Languages & Frameworks: Python, SQL, R, Java, JavaScript, React.js, TypeScript, FastAPI, Django REST) show
40 548 moveto
(AI & Data Science: FAISS Vector Search, FastEmbed, Groq LLM, RAG, Scikit-Learn, Pandas, NumPy) show
40 536 moveto
(Databases & Tools: MySQL, PostgreSQL (3NF), SQLite, Git, GitHub Actions (CI/CD), Docker, Pytest) show

0.8 0.8 0.8 setrgbcolor
40 524 moveto 555 524 lineto stroke
0 setrgbcolor

/Helvetica-Bold findfont 11 scalefont setfont
40 507 moveto
(FEATURED PROJECTS) show

/Helvetica-Bold findfont 9.5 scalefont setfont
40 493 moveto
(DocMind AI -- Production RAG Document Intelligence Platform) show
/Helvetica findfont 9 scalefont setfont
40 481 moveto
(FastAPI | React.js/TypeScript | FAISS | Groq LLM | JWT Auth -- github.com/vivekjpoojary/docmind-ai) show
40 469 moveto
(* Architected full-stack RAG platform with per-user isolated FAISS vector search and page-accurate citations.) show
40 457 moveto
(* Built JWT auth with refresh-token rotation; validated by 33/33 automated tests passing in GitHub Actions CI.) show

/Helvetica-Bold findfont 9.5 scalefont setfont
40 441 moveto
(PlayPoint -- Sports Venue Booking & Analytics Platform) show
/Helvetica findfont 9 scalefont setfont
40 429 moveto
(React.js | Django REST Framework | SQLite 3NF | Scikit-learn) show
40 417 moveto
(* Full-stack booking system with 3-tier JWT RBAC and 3NF schema across 9 normalized tables.) show
40 405 moveto
(* Trained Linear Regression model on booking history to predict peak demand slots for allocation dashboards.) show

/Helvetica-Bold findfont 9.5 scalefont setfont
40 389 moveto
(Website for Immortals -- Sports & Martial Arts Academy Platform) show
/Helvetica findfont 9 scalefont setfont
40 377 moveto
(HTML5 | CSS3 | JavaScript ES6+ | UI/UX Animations | Responsive Web Design) show
40 365 moveto
(* Engineered high-performance web platform with event registration, athlete profiles, and tournament gallery.) show

/Helvetica-Bold findfont 9.5 scalefont setfont
40 349 moveto
(SpaceX Falcon 9 Landing Prediction -- IBM Data Science Capstone) show
/Helvetica findfont 9 scalefont setfont
40 337 moveto
(Python | Pandas | NumPy | Scikit-Learn | Folium) show
40 325 moveto
(* Built end-to-end pipeline predicting booster landing outcomes with 83.3% Decision Tree accuracy & Folium maps.) show

0.8 0.8 0.8 setrgbcolor
40 313 moveto 555 313 lineto stroke
0 setrgbcolor

/Helvetica-Bold findfont 11 scalefont setfont
40 296 moveto
(CERTIFICATIONS & ACHIEVEMENTS) show

/Helvetica findfont 9 scalefont setfont
40 282 moveto
(* IBM Data Science Professional Certificate (IBM / Coursera, Aug 2025)) show
40 270 moveto
(* Deloitte Technology Virtual Experience Program (Forage, Mar 2026)) show
40 258 moveto
(* Introduction to Generative AI Studio (Jul 2026)) show
40 246 moveto
(* Data Formats for Data Engineering and AI (Edvane, Jul 2026)) show
40 234 moveto
(* National-Level Wushu & Kung Fu Athlete -- Bronze Medalist (16th National Kung-Fu Championship)) show
"""
    
    stream_bytes = stream_content.encode('latin1')
    compressed = zlib.compress(stream_bytes)
    
    objects = []
    # Obj 1: Catalog
    objects.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    # Obj 2: Pages
    objects.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    # Obj 3: Page
    objects.append(b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << /Font << /Helvetica 5 0 R /Helvetica-Bold 6 0 R >> >> >>\nendobj\n")
    # Obj 4: Stream
    stream_header = f"4 0 obj\n<< /Length {len(compressed)} /Filter /FlateDecode >>\nstream\n".encode('latin1')
    stream_footer = b"\nendstream\nendobj\n"
    objects.append(stream_header + compressed + stream_footer)
    # Obj 5: Font Helvetica
    objects.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n")
    # Obj 6: Font Helvetica-Bold
    objects.append(b"6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>\nendobj\n")

    # Assemble PDF
    pdf = b"%PDF-1.4\n"
    offsets = []
    for obj in objects:
        offsets.append(len(pdf))
        pdf += obj
    
    xref_offset = len(pdf)
    pdf += f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode('latin1')
    for off in offsets:
        pdf += f"{off:010d} 00000 n \n".encode('latin1')
    
    pdf += f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode('latin1')
    
    with open(filename, "wb") as f:
        f.write(pdf)
    print(f"PDF generated: {filename}")

if __name__ == "__main__":
    create_resume_pdf()
