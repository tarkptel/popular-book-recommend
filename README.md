<section>
        <h1>Project Description</h1>
        <p>This is a Flask-based web application that recommends books based on their popularity and ratings. This Recommend system build based on collaborative filtering approach. The model uses a popularity-based approach to suggest books with the highest ratings. The application is deployed and accessible online via Render.</p>
    </section>
    <!-- Section 2: How to Use -->
    <section>
        <h1>How to Use</h1>
        <p>Live Demo Link - <a href="https://popular-book-recommend-2.onrender.com" target="_blank">https://popular-book-recommend-2.onrender.com</a></p>
        <li>Visit the homepage to see the top recommended books.</li>
         <li>Enter the book name or search criteria in the input box.</li>
         <li>Click "Recommend" to see the suggestions.</li>
    </section>
    <!-- Section 3: Project Structure -->



</head>
<body>
    <div class="container">
        <h1 class="mb-4">Project Structure</h1>
        <p>The project was structured as follows:</p>
        <pre>
├── script.py            # Main Flask application file to run the web app
├── templates/           # Folder for HTML templates used by the Flask app
│   ├── recommend.html   # Home page of the book recommender system
│   ├── ts.html          # Result page for displaying recommendations
├── notebook/            # Jupyter Notebook
     ├── jupyterFile.jpynb      
├── model_files/         # Folder containing pre-processed data and similarity files
│   ├── pivot_table.pkl  # Pivot table used for recommendations
│   ├── similarity.pkl   # Pre-calculated similarity scores
│   ├── book.pkl.pkl     # Most Popular 50 Books          
├── README.md            # Project documentation and usage instructions
├── Procfile             # Configuration file for deploying on Render
├── requirements.txt     # Python version specification for Render
├── LICENSE              # MIT LICENSE
        </pre>
        <p class="text-muted"># Each folder and file serves a specific purpose in the project's lifecycle.</p>
    </div>
</body>
</html>
   
  <h1>Dataset</h1>

<p>This project utilizes a book recommendation dataset from Kaggle. You can access the dataset for further exploration and experimentation here:</p>

<p> 
   <b>Kaggle - </b> <a href="https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset"> Dataset Link</a>
</p>

 </section>
   <h1>Model Training Approach</h1>
        <ul>
            <li><code><strong>[popular_book]</strong></code>: - 50 most popular books based on rating and votes.</li>
            <li><code><strong>[stan_df]</strong></code>: - Finding Those Users who rated more than 200 different books.</li>
            <li><code><strong>[rating_50_book]</strong></code>: - Finding those Books which have more than 50 Rating Count (more than 50 different user rated this book).</li>
            <li><code><strong>[pt]</strong></code>: - Pivot table for [rating_50_book] based on ratings and votes.</li>
            <li><code><strong>[similarity_s]</strong></code>: - Calculated similarity score between [rating_50_book]'s all books.</li>
        </ul>
        <p>After, I created a function that takes a book name and gives 6 most related books.</p>

      
  </section>
    <!-- Section 5: Deploying -->
    <section>
        <h1>Deploying Through Render</h1>
        
  <p>I Deploy my model through Render.com.</p>

  <h3>Steps:</h3>
  <ol>
    <li><strong>Render Setup:</strong> Create a Render.com account and a new "Web Service."</li>
    <li><strong>Connect GitHub:</strong> Connect your Render service to this GitHub repository.</li>
    <li><strong>Configure:</strong> Review/adjust build commands (usually auto-detected for Python). Set any necessary environment variables.</li>
    <li><strong>Deploy:</strong> Click "Deploy." Render will build and deploy your app.</li>
    <li><strong>Access:</strong> Use the provided Render URL to access your deployed system.</li>
  </ol>
    </section>
    <!-- Section 6: Author -->
    <section>
        <h1>Author</h1>
        <p>Developed by <b><a</b>Tark Patel<a/></a></b>
        <ul>
          <li><b><a href="https://www.linkedin.com/in/tarkpatel">LinkedIn</a></b></li>
          <li><b><a href="https://www.kaggle.com/tarkpatel">Kaggle</a></b></li>
        </ul>

    
</body>
</html>
