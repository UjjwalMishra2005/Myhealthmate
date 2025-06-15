const dropdownToggle = document.getElementById('dropdownToggle');
        const dropdownMenu = document.getElementById('dropdownMenu');

        dropdownToggle.addEventListener('click', function(e) {
            e.preventDefault();
            dropdownMenu.classList.toggle('hidden');
        });

        // Mobile menu toggle functionality
        const mobileMenuToggle = document.getElementById('mobileMenuToggle');
        const mobileMenu = document.getElementById('mobileMenu');
        const line1 = document.getElementById('line1');
        const line2 = document.getElementById('line2');
        const line3 = document.getElementById('line3');

        mobileMenuToggle.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
            
            // Toggle hamburger animation
            if (mobileMenu.classList.contains('hidden')) {
                line1.style.transform = 'translateY(6px)';
                line2.style.opacity = '1';
                line3.style.transform = 'translateY(-6px)';
            } else {
                line1.style.transform = 'rotate(45deg) translateY(0)';
                line2.style.opacity = '0';
                line3.style.transform = 'rotate(-45deg) translateY(0)';
            }
        });

        // Close dropdowns when clicking outside
        document.addEventListener('click', function(e) {
            if (!dropdownToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
                dropdownMenu.classList.add('hidden');
            }
            
            if (!mobileMenuToggle.contains(e.target) && !mobileMenu.contains(e.target)) {
                mobileMenu.classList.add('hidden');
                // Reset hamburger lines
                line1.style.transform = 'translateY(6px)';
                line2.style.opacity = '1';
                line3.style.transform = 'translateY(-6px)';
            }
        });

        const floatingBox = document.getElementById("floatingBox");
        const boxHeader = document.getElementById("boxHeader");
        const closeBtn = document.getElementById("closeBox");

            let isDragging = false;
            let offsetX = 0;
            let offsetY = 0;

            // Hide floating box with smooth animation
            function hideFloatingBox() {
                floatingBox.style.transform = 'translateY(-20px) scale(0.9)';
                floatingBox.style.opacity = '0';
                
                setTimeout(() => {
                    floatingBox.style.display = 'none';
                }, 300);
            }

            // Dragging functionality with smooth movements
            boxHeader.addEventListener("mousedown", (e) => {
                isDragging = true;
                offsetX = e.clientX - floatingBox.offsetLeft;
                offsetY = e.clientY - floatingBox.offsetTop;
                boxHeader.style.cursor = "grabbing";
                document.body.classList.add('dragging');
                floatingBox.classList.add('dragging');
            });

            document.addEventListener("mouseup", () => {
                if (isDragging) {
                    isDragging = false;
                    boxHeader.style.cursor = "grab";
                    document.body.classList.remove('dragging');
                    floatingBox.classList.remove('dragging');
                }
            });

            document.addEventListener("mousemove", (e) => {
                if (!isDragging) return;
                
                e.preventDefault();
                let newX = e.clientX - offsetX;
                let newY = e.clientY - offsetY;
                
                // Keep within viewport bounds with smooth constraint
                const maxX = window.innerWidth - floatingBox.offsetWidth;
                const maxY = window.innerHeight - floatingBox.offsetHeight;
                
                newX = Math.max(0, Math.min(newX, maxX));
                newY = Math.max(0, Math.min(newY, maxY));
                
                // Use transform for smoother movement
                floatingBox.style.left = `${newX}px`;
                floatingBox.style.top = `${newY}px`;
            });

            // Close button functionality
            closeBtn.addEventListener("click", hideFloatingBox);

            // Close with Escape key
            document.addEventListener("keydown", (e) => {
                if (e.key === "Escape" && floatingBox.style.display !== 'none') {
                    hideFloatingBox();
                }
            });

            // Prevent text selection while dragging
            boxHeader.addEventListener("selectstart", (e) => {
                if (isDragging) e.preventDefault();
            });

            // Smooth resize handling
            window.addEventListener('resize', () => {
                if (!isDragging) {
                    const rect = floatingBox.getBoundingClientRect();
                    const maxX = window.innerWidth - floatingBox.offsetWidth;
                    const maxY = window.innerHeight - floatingBox.offsetHeight;
                    
                    if (rect.left > maxX) {
                        floatingBox.style.left = `${maxX}px`;
                    }
                    if (rect.top > maxY) {
                        floatingBox.style.top = `${maxY}px`;
                    }
                }
            });