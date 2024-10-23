document.addEventListener("DOMContentLoaded", function () {
    const scrollToTopButton = document.getElementById("scroll-to-top");

        window.addEventListener("scroll", () => {
            if (window.scrollY > 300) {
                scrollToTopButton.classList.remove("hidden");
                scrollToTopButton.style.opacity = "1"; // Tornar visível
                scrollToTopButton.style.transition = "opacity 1s ease-in-out"; // Efeito de fade-in
            } else {
                scrollToTopButton.style.opacity = "0"; // Tornar invisível
                scrollToTopButton.style.transition = "opacity 1s ease-in-out"; // Efeito de fade-out
                setTimeout(() => {
                    scrollToTopButton.classList.add("hidden");
                }, 500); // Esperar a animação terminar antes de esconder completamente
            }
        });

        scrollToTopButton.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth", // Efeito suave ao voltar ao topo
            });
        });
});