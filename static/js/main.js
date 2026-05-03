// Toast initialization
document.addEventListener('DOMContentLoaded', function () {
    // Existing toasts
    var toastElList = [].slice.call(document.querySelectorAll('.toast'))
    var toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl, { delay: 5000 })
    });

    // Live Search Logic
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');

    if (searchInput) {
        searchInput.addEventListener('input', async (e) => {
            const query = e.target.value.trim();
            if (query.length < 2) {
                searchResults.style.display = 'none';
                return;
            }

            try {
                const response = await fetch(`/api/products/api/?search=${query}`);
                const data = await response.json();

                if (data.results && data.results.length > 0) {
                    searchResults.innerHTML = data.results.slice(0, 5).map(p => `
                        <a href="/api/products/${p.slug}/" class="dropdown-item d-flex align-items-center py-3 border-bottom">
                            <i class="fas fa-shopping-bag me-3 text-secondary opacity-50"></i>
                            <div>
                                <p class="mb-0 fw-bold small">${p.name}</p>
                                <small class="text-primary-custom">₦${p.price}</small>
                            </div>
                        </a>
                    `).join('') + `<a href="/api/products/?search=${query}" class="dropdown-item text-center py-2 bg-light small fw-bold">View all results</a>`;
                    searchResults.style.display = 'block';
                } else {
                    searchResults.style.display = 'none';
                }
            } catch (err) {
                console.error('Search failed', err);
            }
        });

        // Hide search on click outside
        document.addEventListener('click', (e) => {
            if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
                searchResults.style.display = 'none';
            }
        });
    }
});
