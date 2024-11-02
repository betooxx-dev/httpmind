// index.js
document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("searchInput");
  const searchButton = document.getElementById("searchButton");
  const loader = document.getElementById("loader");
  const resultDiv = document.getElementById("result");
  const container = document.querySelector(".container");

  function showLoader() {
    loader.style.display = "block";
    resultDiv.style.display = "none";
    searchButton.disabled = true;
  }

  function hideLoader() {
    loader.style.display = "none";
    searchButton.disabled = false;
  }

  function clearResults() {
    resultDiv.style.display = "none";
    resultDiv.innerHTML = "";
    container.classList.remove("results-shown");
  }

  function showResult(data) {
    resultDiv.style.display = "block";
    container.classList.add("results-shown");

    resultDiv.innerHTML = `
            <h2>${data.code} - ${data.title}</h2>
            <p><strong>Tipo:</strong> ${data.type}</p>
            <p><strong>Descripción:</strong> ${data.description}</p>
            <div class="solutions">
                <strong>Soluciones:</strong>
                <ul>
                    ${data.solutions
                      .map((solution) => `<li>${solution}</li>`)
                      .join("")}
                </ul>
            </div>
            <div class="severity ${data.severity}">
                Severidad: ${data.severity}
            </div>
        `;
  }

  function showError(message) {
    resultDiv.style.display = "block";
    container.classList.remove("results-shown");

    resultDiv.innerHTML = `
            <h2>Error</h2>
            <p>${message}</p>
        `;
  }

  function validateInput(value) {
    const isValidCode = /^\d{3}$/.test(value);
    searchButton.disabled = !isValidCode;
    return isValidCode;
  }

  async function searchHttpCode() {
    const code = searchInput.value;
    if (!validateInput(code)) return;

    showLoader();
    try {
      const response = await fetch(`/api/status/${code}`);
      const data = await response.json();
      hideLoader();

      if (response.ok) {
        showResult(data);
      } else {
        showError(data.message);
      }
    } catch (error) {
      hideLoader();
      showError("Error al conectar con el servidor");
    }
  }

  // Event Listeners
  searchInput.addEventListener("input", (e) => {
    validateInput(e.target.value);
    clearResults(); // Limpia los resultados cuando el input cambia
  });

  searchButton.addEventListener("click", searchHttpCode);

  searchInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter" && !searchButton.disabled) {
      searchHttpCode();
    }
  });
});
