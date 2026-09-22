document.addEventListener('DOMContentLoaded', () => {
    const navButtons = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.model-card');

    navButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active classes
            navButtons.forEach(b => b.classList.remove('active'));
            sections.forEach(s => {
                s.classList.remove('active');
                s.classList.remove('fade-in');
            });

            // Add active class to clicked button
            btn.classList.add('active');
            
            // Show corresponding section
            const targetId = btn.getAttribute('data-target');
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                targetSection.classList.add('active');
                
                // Force reflow to restart the CSS animation smoothly
                void targetSection.offsetWidth;
                
                targetSection.classList.add('fade-in');
            }
        });
    });
});
