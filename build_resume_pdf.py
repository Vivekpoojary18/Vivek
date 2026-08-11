import zlib

def create_resume_pdf(filename="Vivek_J_Poojary_Resume.pdf"):
    # Generate exact PDF matching Vivek J Poojary's official resume PDF
    lines = [
        # Title
        ("/Helvetica-Bold", 20, 45, 760, "VIVEK J POOJARY"),
        ("/Helvetica", 8.5, 45, 746, "Mangaluru, Karnataka, India | vivekjpoojary@gmail.com | +91 82173 67683 | linkedin.com/in/vivekjpoojary | github.com/Vivekjpoojary"),
        ("LINE", 45, 738, 550, 738),
        
        # SUMMARY
        ("/Helvetica-Bold", 10.5, 45, 725, "SUMMARY"),
        ("/Helvetica", 8.5, 45, 712, "Builds and ships systems that turn raw data into decisions -- from a retrieval-augmented AI platform serving page-accurate answers across documents to"),
        ("/Helvetica", 8.5, 45, 701, "a demand-forecasting engine that directly shapes real-time resource allocation. Track record centers on closing the gap between prototype and production:"),
        ("/Helvetica", 8.5, 45, 690, "33/33 automated tests passing in CI, an 83.3% predictive accuracy benchmark achieved through systematic model comparison, and normalized data"),
        ("/Helvetica", 8.5, 45, 679, "architectures built to eliminate redundancy at scale. IBM-certified Data Science practitioner (BCA, CGPA 8.08) seeking an entry-level Data Analyst,"),
        ("/Helvetica", 8.5, 45, 668, "Data Science, or AI/ML Engineering role."),
        ("LINE", 45, 660, 550, 660),

        # EDUCATION
        ("/Helvetica-Bold", 10.5, 45, 647, "EDUCATION"),
        ("/Helvetica-Bold", 9, 45, 634, "Bachelor of Computer Applications (BCA)"),
        ("/Helvetica-Oblique", 8.5, 230, 634, "Jun 2023 -- May 2026"),
        ("/Helvetica-Oblique", 8.5, 45, 623, "St. Aloysius (Deemed to be University), Mangaluru, Karnataka"),
        ("/Helvetica", 8.5, 55, 611, "* CGPA: 8.08 / 10.0"),
        ("/Helvetica", 8.5, 55, 600, "* Relevant Coursework: Data Structures, Database Management Systems, Machine Learning Fundamentals, Statistical Analysis, Web Technologies"),
        ("LINE", 45, 592, 550, 592),

        # TECHNICAL SKILLS
        ("/Helvetica-Bold", 10.5, 45, 579, "TECHNICAL SKILLS"),
        ("/Helvetica", 8.5, 55, 566, "* Programming Languages: Python, SQL, R, Java, JavaScript, PHP, C"),
        ("/Helvetica", 8.5, 55, 555, "* ML / Data Science: Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Predictive Modelling, Feature Engineering"),
        ("/Helvetica", 8.5, 55, 544, "* AI / RAG: FAISS Vector Search, FastEmbed, LLM Integration (Groq), Retrieval-Augmented Generation"),
        ("/Helvetica", 8.5, 55, 533, "* Web Technologies: HTML5, CSS3, JavaScript, React.js, TypeScript, TailwindCSS, PHP, J2EE, REST APIs, FastAPI, Django REST Framework"),
        ("/Helvetica", 8.5, 55, 522, "* Databases: MySQL, SQLite, PostgreSQL (3NF schema design, complex joins, indexing)"),
        ("/Helvetica", 8.5, 55, 511, "* Tools & Platforms: Jupyter Notebook, Git, GitHub, GitHub Actions (CI/CD), Docker-ready deployments (Render, Vercel), VS Code"),
        ("/Helvetica", 8.5, 55, 500, "* Concepts: Machine Learning, Data Analysis, JWT-based Auth & RBAC Systems, Geospatial Visualisation, Automated Testing (pytest)"),
        ("LINE", 45, 492, 550, 492),

        # PROJECTS
        ("/Helvetica-Bold", 10.5, 45, 479, "PROJECTS"),
        ("/Helvetica-Bold", 9, 45, 466, "DocMind AI -- Production RAG Document Intelligence Platform"),
        ("/Helvetica-Oblique", 8.5, 305, 466, "FastAPI | React.js/TypeScript | FAISS | Groq LLM | JWT Auth -- github.com/vivekjpoojary/docmind-ai"),
        ("/Helvetica", 8.5, 55, 455, "* Architected and deployed a full-stack RAG platform (FastAPI + React/TypeScript, live on Render and Vercel) enabling PDF/DOCX/TXT upload"),
        ("/Helvetica", 8.5, 63, 444, "and AI-powered Q&A with page-accurate citations."),
        ("/Helvetica", 8.5, 55, 433, "* Implemented per-user isolated FAISS vector search with FastEmbed embeddings and Groq LLM integration for low-latency retrieval augmented generation."),
        ("/Helvetica", 8.5, 55, 422, "* Built JWT-based auth with refresh-token rotation and rate limiting; validated with 33/33 automated tests passing via GitHub Actions CI."),

        ("/Helvetica-Bold", 9, 45, 407, "PlayPoint -- Sports Venue Booking & Analytics Platform"),
        ("/Helvetica-Oblique", 8.5, 275, 407, "React.js | Django REST Framework | SQLite | Python | Scikit-learn -- github.com/Vivekjpoojary"),
        ("/Helvetica", 8.5, 55, 396, "* Built a full-stack booking platform for real-time court reservations, supporting three permission tiers via a JWT-based Role-Based Access Control system."),
        ("/Helvetica", 8.5, 55, 385, "* Designed a 3NF-compliant relational schema across nine normalized tables, enforcing referential integrity and eliminating redundant data across all modules."),
        ("/Helvetica", 8.5, 55, 374, "* Trained a Linear Regression model on historical booking data to predict peak-demand slots, feeding directly into slot allocation and dashboards."),

        ("/Helvetica-Bold", 9, 45, 359, "IBM Data Science Capstone -- Falcon 9 Landing Prediction"),
        ("/Helvetica-Oblique", 8.5, 290, 359, "Python | Pandas | NumPy | Scikit-learn | Matplotlib | Folium"),
        ("/Helvetica", 8.5, 55, 348, "* Built an end-to-end pipeline -- SpaceX REST API ingestion and web scraping, EDA, feature engineering, and modelling -- to predict landing outcomes."),
        ("/Helvetica", 8.5, 55, 337, "* Benchmarked four classifiers (Logistic Regression, Decision Tree, SVM, KNN); a GridSearchCV-tuned Decision Tree achieved 83.3% accuracy."),
        ("/Helvetica", 8.5, 55, 326, "* Built interactive Folium maps to visualise launch-site proximity and surface spatial patterns across historical missions."),
        ("LINE", 45, 318, 550, 318),

        # CERTIFICATIONS
        ("/Helvetica-Bold", 10.5, 45, 305, "CERTIFICATIONS"),
        ("/Helvetica-Bold", 9, 45, 292, "IBM Data Science Professional Certificate"),
        ("/Helvetica-Oblique", 8.5, 240, 292, "Aug 2025"),
        ("/Helvetica-Oblique", 8.5, 45, 281, "IBM / Coursera"),
        ("/Helvetica", 8.5, 55, 270, "* 10-course specialisation covering Python, SQL, data visualisation, and machine learning, capped by an applied capstone spanning full lifecycle."),

        ("/Helvetica-Bold", 9, 45, 255, "Deloitte Technology Virtual Experience Program"),
        ("/Helvetica-Oblique", 8.5, 250, 255, "Mar 2026"),
        ("/Helvetica-Oblique", 8.5, 45, 244, "Forage"),
        ("/Helvetica", 8.5, 55, 233, "* Completed hands-on modules in Python-based ETL, IIoT data unification, and software architecture proposal for simulated client engagement."),
        ("LINE", 45, 225, 550, 225),

        # ACHIEVEMENTS & ACTIVITIES
        ("/Helvetica-Bold", 10.5, 45, 212, "ACHIEVEMENTS & ACTIVITIES"),
        ("/Helvetica", 8.5, 55, 199, "* National-Level Wushu & Kung Fu Athlete -- Bronze medal, 16th National Kung-Fu Championship; multiple national-level participations."),
        ("/Helvetica", 8.5, 55, 188, "* Class Representative (2024--25) -- Elected student liaison between faculty and peers for a BCA cohort, handling academic communications.")
    ]

    ps_code = []
    for item in lines:
        if item[0] == "LINE":
            _, x1, y1, x2, y2 = item
            ps_code.append(f"0.75 setgray {x1} {y1} moveto {x2} {y2} lineto stroke 0 setgray\n")
        else:
            font, size, x, y, text = item
            escaped_text = text.replace("(", "\\(").replace(")", "\\)")
            ps_code.append(f"{font} findfont {size} scalefont setfont {x} {y} moveto ({escaped_text}) show\n")

    stream_content = "".join(ps_code)
    stream_bytes = stream_content.encode('latin1')
    compressed = zlib.compress(stream_bytes)

    objects = []
    objects.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    objects.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    objects.append(b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << /Font << /Helvetica 5 0 R /Helvetica-Bold 6 0 R /Helvetica-Oblique 7 0 R >> >> >>\nendobj\n")
    
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

    with open(filename, "wb") as f:
        f.write(pdf)
    print(f"Exact Resume PDF generated: {filename}")

if __name__ == "__main__":
    create_resume_pdf()
