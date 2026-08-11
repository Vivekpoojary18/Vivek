import zlib

def make_valid_pdf():
    elements = []

    # Title & Contact Header
    elements.append("BT /F2 18 Tf 1 0 0 1 40 800 Tm (VIVEK J POOJARY) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 40 784 Tm (Mangaluru, Karnataka, India | vivekjpoojary@gmail.com | +91 82173 67683 | linkedin.com/in/vivekjpoojary | github.com/Vivekjpoojary) Tj ET\n")
    elements.append("0.75 setgray 0.75 w 40 776 m 555 776 l S 0 setgray\n")

    # SUMMARY
    elements.append("BT /F2 10 Tf 1 0 0 1 40 762 Tm (SUMMARY) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 40 749 Tm (Builds and ships systems that turn raw data into decisions -- from a retrieval-augmented AI platform serving page-accurate answers) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 40 738 Tm (across documents to a demand-forecasting engine that directly shapes real-time resource allocation. Track record centers on closing) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 40 727 Tm (the gap between prototype and production: 33/33 automated tests passing in CI, an 83.3% predictive accuracy benchmark achieved) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 40 716 Tm (through systematic model comparison, and normalized data architectures built to eliminate redundancy at scale. IBM-certified Data) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 40 705 Tm (Science practitioner \\(BCA, CGPA 8.08\\) seeking an entry-level Data Analyst, Data Science, or AI/ML Engineering role.) Tj ET\n")
    elements.append("0.75 setgray 0.75 w 40 697 m 555 697 l S 0 setgray\n")

    # EDUCATION
    elements.append("BT /F2 10 Tf 1 0 0 1 40 683 Tm (EDUCATION) Tj ET\n")
    elements.append("BT /F2 9 Tf 1 0 0 1 40 670 Tm (Bachelor of Computer Applications \\(BCA\\)) Tj ET\n")
    elements.append("BT /F3 8.5 Tf 1 0 0 1 450 670 Tm (Jun 2023 - May 2026) Tj ET\n")
    elements.append("BT /F3 8.5 Tf 1 0 0 1 40 659 Tm (St. Aloysius \\(Deemed to be University\\), Mangaluru, Karnataka) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 647 Tm (\\225  CGPA: 8.08 / 10.0) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 636 Tm (\\225  Relevant Coursework: Data Structures, DBMS, Machine Learning Fundamentals, Statistical Analysis, Web Technologies) Tj ET\n")
    elements.append("0.75 setgray 0.75 w 40 628 m 555 628 l S 0 setgray\n")

    # TECHNICAL SKILLS
    elements.append("BT /F2 10 Tf 1 0 0 1 40 614 Tm (TECHNICAL SKILLS) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 601 Tm (\\225  Programming Languages: Python, SQL, R, Java, JavaScript, PHP, C) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 590 Tm (\\225  ML / Data Science: Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Predictive Modelling, Feature Engineering) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 579 Tm (\\225  AI / RAG: FAISS Vector Search, FastEmbed, LLM Integration \\(Groq\\), Retrieval-Augmented Generation) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 568 Tm (\\225  Web Technologies: HTML5, CSS3, JavaScript, React.js, TypeScript, TailwindCSS, PHP, REST APIs, FastAPI, Django REST) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 557 Tm (\\225  Databases: MySQL, SQLite, PostgreSQL \\(3NF schema design, complex joins, indexing\\)) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 546 Tm (\\225  Tools & Platforms: Jupyter Notebook, Git, GitHub, GitHub Actions \\(CI/CD\\), Docker deployments, Render, Vercel, VS Code) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 535 Tm (\\225  Concepts: Machine Learning, Data Analysis, JWT Auth & RBAC Systems, Geospatial Visualisation, Automated Testing \\(pytest\\)) Tj ET\n")
    elements.append("0.75 setgray 0.75 w 40 527 m 555 527 l S 0 setgray\n")

    # PROJECTS
    elements.append("BT /F2 10 Tf 1 0 0 1 40 513 Tm (PROJECTS) Tj ET\n")
    elements.append("BT /F2 9 Tf 1 0 0 1 40 500 Tm (DocMind AI -- Production RAG Document Intelligence Platform) Tj ET\n")
    elements.append("BT /F3 8.5 Tf 1 0 0 1 40 489 Tm (FastAPI | React.js/TypeScript | FAISS | Groq LLM | JWT Auth -- github.com/vivekjpoojary/docmind-ai) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 478 Tm (\\225  Architected & deployed full-stack RAG platform enabling PDF/DOCX/TXT upload & AI Q&A with page-accurate citations.) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 467 Tm (\\225  Implemented per-user isolated FAISS vector search with FastEmbed embeddings and Groq LLM integration.) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 456 Tm (\\225  Built JWT-based auth with refresh-token rotation; validated with 33/33 automated tests passing via GitHub Actions CI.) Tj ET\n")

    elements.append("BT /F2 9 Tf 1 0 0 1 40 441 Tm (PlayPoint -- Sports Venue Booking & Analytics Platform) Tj ET\n")
    elements.append("BT /F3 8.5 Tf 1 0 0 1 40 430 Tm (React.js | Django REST Framework | SQLite | Python | Scikit-learn -- github.com/Vivekjpoojary) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 419 Tm (\\225  Built full-stack booking platform for court reservations supporting three permission tiers via JWT RBAC.) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 408 Tm (\\225  Designed 3NF-compliant relational schema across nine normalized tables enforcing referential integrity.) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 397 Tm (\\225  Trained Linear Regression model on booking history to predict peak-demand slots feeding slot-allocation dashboards.) Tj ET\n")

    elements.append("BT /F2 9 Tf 1 0 0 1 40 382 Tm (IBM Data Science Capstone -- Falcon 9 Landing Prediction) Tj ET\n")
    elements.append("BT /F3 8.5 Tf 1 0 0 1 40 371 Tm (Python | Pandas | NumPy | Scikit-learn | Matplotlib | Folium) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 360 Tm (\\225  Built end-to-end pipeline -- SpaceX REST API ingestion, web scraping, EDA, and feature engineering.) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 349 Tm (\\225  Benchmarked four classifiers; a GridSearchCV-tuned Decision Tree achieved 83.3% accuracy, the best of the set.) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 338 Tm (\\225  Built interactive Folium maps to visualise launch-site proximity and surface spatial patterns across historical missions.) Tj ET\n")
    elements.append("0.75 setgray 0.75 w 40 330 m 555 330 l S 0 setgray\n")

    # CERTIFICATIONS
    elements.append("BT /F2 10 Tf 1 0 0 1 40 316 Tm (CERTIFICATIONS) Tj ET\n")
    elements.append("BT /F2 9 Tf 1 0 0 1 40 303 Tm (IBM Data Science Professional Certificate) Tj ET\n")
    elements.append("BT /F3 8.5 Tf 1 0 0 1 490 303 Tm (Aug 2025) Tj ET\n")
    elements.append("BT /F3 8.5 Tf 1 0 0 1 40 292 Tm (IBM / Coursera) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 281 Tm (\\225  10-course specialisation covering Python, SQL, data visualisation, and ML, capped by applied capstone project.) Tj ET\n")

    elements.append("BT /F2 9 Tf 1 0 0 1 40 266 Tm (Deloitte Technology Virtual Experience Program) Tj ET\n")
    elements.append("BT /F3 8.5 Tf 1 0 0 1 490 266 Tm (Mar 2026) Tj ET\n")
    elements.append("BT /F3 8.5 Tf 1 0 0 1 40 255 Tm (Forage) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 244 Tm (\\225  Completed modules in Python-based ETL, IIoT data unification, and software architecture proposal.) Tj ET\n")
    elements.append("0.75 setgray 0.75 w 40 236 m 555 236 l S 0 setgray\n")

    # ACHIEVEMENTS & ACTIVITIES
    elements.append("BT /F2 10 Tf 1 0 0 1 40 222 Tm (ACHIEVEMENTS & ACTIVITIES) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 209 Tm (\\225  National-Level Wushu & Kung Fu Athlete -- Bronze medal, 16th National Kung-Fu Championship.) Tj ET\n")
    elements.append("BT /F1 8.5 Tf 1 0 0 1 50 198 Tm (\\225  Class Representative \\(2024-25\\) -- Elected student liaison between faculty and peers for a BCA cohort.) Tj ET\n")

    stream_content = "".join(elements)
    stream_bytes = stream_content.encode('latin1')
    compressed = zlib.compress(stream_bytes)

    objects = []
    objects.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    objects.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    objects.append(b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R /F3 7 0 R >> >> >>\nendobj\n")
    
    stream_header = f"4 0 obj\n<< /Length {len(compressed)} /Filter /FlateDecode >>\nstream\n".encode('latin1')
    stream_footer = b"\nendstream\nendobj\n"
    objects.append(stream_header + compressed + stream_footer)

    objects.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n")
    objects.append(b"6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>\nendobj\n")
    objects.append(b"7 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique >>\nendobj\n")

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

    with open("Vivek_J_Poojary_Resume.pdf", "wb") as f:
        f.write(pdf)
    print("Refined PDF 1.4 generated!")

if __name__ == '__main__':
    make_valid_pdf()
