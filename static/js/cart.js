// Simple Cart Logic
const Cart = {
    items: JSON.parse(localStorage.getItem('vellon_cart')) || [],

    add(product) {
        const existing = this.items.find(item => item.id === product.id);
        if (existing) {
            existing.quantity += 1;
        } else {
            this.items.push({ ...product, quantity: 1 });
        }
        this.save();
        this.render();
        this.showToast(`${product.name} added to cart!`);
    },

    remove(id) {
        this.items = this.items.filter(item => item.id !== id);
        this.save();
        this.render();
    },

    save() {
        localStorage.setItem('vellon_cart', JSON.stringify(this.items));
    },

    render() {
        const cartContainer = document.getElementById('cart-items');
        const cartCount = document.getElementById('cart-count');
        const cartTotal = document.getElementById('cart-total');

        if (!cartContainer) return;

        cartCount.innerText = this.items.reduce((sum, item) => sum + item.quantity, 0);

        if (this.items.length === 0) {
            cartContainer.innerHTML = `
                <div class="text-center py-5 opacity-50">
                    <i class="fas fa-shopping-basket fa-3x mb-3"></i>
                    <p>Your cart is empty</p>
                </div>`;
            cartTotal.innerText = '₦0';
            return;
        }

        let total = 0;
        cartContainer.innerHTML = this.items.map(item => {
            total += item.price * item.quantity;
            return `
                <div class="d-flex gap-3 mb-4 align-items-center">
                    <div style="width: 60px; height: 60px; background: var(--bg-soft); border-radius: var(--radius-sm);" class="d-flex align-items-center justify-content-center">
                        <i class="fas fa-image text-muted"></i>
                    </div>
                    <div class="flex-grow-1">
                        <h6 class="mb-0 fw-bold small">${item.name}</h6>
                        <small class="text-secondary">${item.quantity} x ₦${item.price}</small>
                    </div>
                    <button class="btn btn-sm text-danger" onclick="Cart.remove(${item.id})"><i class="fas fa-trash"></i></button>
                </div>`;
        }).join('');

        cartTotal.innerText = `₦${total.toLocaleString()}`;
    },

    showToast(msg) {
        const toastHtml = `
            <div class="toast show border-0 shadow-lg" role="alert">
                <div class="toast-header bg-primary-custom text-white">
                    <strong class="me-auto">Notification</strong>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast"></button>
                </div>
                <div class="toast-body bg-white">${msg}</div>
            </div>`;
        const container = document.querySelector('.toast-container');
        if (container) {
            container.insertAdjacentHTML('beforeend', toastHtml);
            const newToast = container.lastElementChild;
            setTimeout(() => newToast.remove(), 5000);
        }
    }
};

document.addEventListener('DOMContentLoaded', () => Cart.render());
window.Cart = Cart; // Make global for onclick
