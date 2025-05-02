import { useState } from 'react';

export default function CvMatcher() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const form = new FormData(e.target);
    const res = await fetch('http://localhost:5000/match', {
      method: 'POST',
      body: form,
    });

    const data = await res.json();
    setResults(data);
    setLoading(false);
  };

  return (
    <div className="container mt-5">
      <div className="card shadow">
        <div className="card-body">
          <h2 className="card-title mb-4">Comparer les CVs avec une fiche de poste</h2>
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">Fiche de poste</label>
              <input type="file" name="job" className="form-control" required />
            </div>
            <div className="mb-3">
              <label className="form-label">CVs</label>
              <input type="file" name="cvs" className="form-control" multiple required />
            </div>
            <button type="submit" >
              {loading ? 'Chargement...' : 'Lancer la comparaison'}
            </button>
          </form>
        </div>
      </div>

      {results.length > 0 && (
        <div className="mt-4">
          <h4>Résultats :</h4>
          {results.map((cv, idx) => (
            <div className="card mb-2" key={idx}>
              <div className="card-body">
                <h5 className="card-title">{cv.filename}</h5>
                <p className="card-text">Score : <strong>{cv.score}%</strong></p>
                <p className="card-text text-muted">
                  Mots-clés : {cv.matched_keywords.join(', ')}
                </p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
