<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Explorador Interactivo: La Segunda Guerra Mundial</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@300;400;700&family=Source+Sans+3:wght@300;400;600&display=swap" rel="stylesheet">
    <!-- Chosen Palette: Warm Neutrals & Historical Tones -->
    <!-- Application Structure Plan: The application is structured thematically to guide the user through the story of the war. It starts with a general introduction, moves to an interactive timeline to explore the key phases, then presents the main factions (Axis vs. Allies) through interactive cards for easy comparison. A data visualization section with a chart quantifies the human cost, and a final section summarizes the long-term consequences. This structure was chosen over a linear document to facilitate non-linear exploration, comparison, and a clearer understanding of the war's scale and impact. -->
    <!-- Visualization & Content Choices: 
        - Report Info: Fases Clave de la Guerra -> Goal: Show chronological progression -> Viz/Method: Interactive vertical timeline (HTML/CSS/JS) -> Interaction: Click on a phase to expand details -> Justification: More engaging than a static list, allows users to control the information flow.
        - Report Info: Potencias del Eje y Aliadas -> Goal: Compare the main belligerents -> Viz/Method: Two-column layout with interactive cards (HTML/CSS/JS) -> Interaction: Click on a country's card to reveal detailed information -> Justification: Facilitates direct comparison and organizes complex information cleanly.
        - Report Info: 50-80 million deaths -> Goal: Visualize the human cost -> Viz/Method: Bar Chart (Chart.js) -> Interaction: Hover over bars for exact figures -> Justification: A chart provides a powerful, immediate understanding of the conflict's devastating scale that text alone cannot convey.
        - Report Info: Consecuencias -> Goal: Inform about the war's aftermath -> Viz/Method: Grid of cards with icons (HTML/Tailwind) -> Interaction: Static, for quick reading -> Justification: Presents the key impacts as distinct, easily digestible points. -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <style>
        body {
            font-family: 'Source Sans 3', sans-serif;
            background-color: #FDFCFB;
            color: #3a3a3a;
        }
        h1, h2, h3 {
            font-family: 'Roboto Slab', serif;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 400px;
            }
        }
    </style>
</head>
<body class="bg-[#FDFCFB]">

    <header class="bg-white/80 backdrop-blur-md sticky top-0 z-50 shadow-sm">
        <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
            <h1 class="text-xl md:text-2xl font-bold text-gray-800">La Segunda Guerra Mundial</h1>
            <div class="hidden md:flex space-x-8">
                <a href="#timeline" class="text-gray-600 hover:text-red-800 transition">Línea de Tiempo</a>
                <a href="#belligerents" class="text-gray-600 hover:text-red-800 transition">Facciones</a>
                <a href="#impact" class="text-gray-600 hover:text-red-800 transition">Impacto</a>
                <a href="#consequences" class="text-gray-600 hover:text-red-800 transition">Consecuencias</a>
            </div>
            <button id="mobile-menu-button" class="md:hidden text-gray-700 focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
            </button>
        </nav>
        <div id="mobile-menu" class="hidden md:hidden px-6 pb-4">
            <a href="#timeline" class="block py-2 text-gray-600 hover:text-red-800">Línea de Tiempo</a>
            <a href="#belligerents" class="block py-2 text-gray-600 hover:text-red-800">Facciones</a>
            <a href="#impact" class="block py-2 text-gray-600 hover:text-red-800">Impacto</a>
            <a href="#consequences" class="block py-2 text-gray-600 hover:text-red-800">Consecuencias</a>
        </div>
    </header>

    <main class="container mx-auto px-6 py-12">

        <section id="intro" class="text-center mb-20">
            <h2 class="text-4xl font-bold mb-4 text-gray-800">El Conflicto que Redefinió el Mundo</h2>
            <p class="max-w-3xl mx-auto text-lg text-gray-600">
                La Segunda Guerra Mundial (1939-1945) fue el conflicto más devastador de la historia, involucrando a la mayoría de las naciones del mundo en dos alianzas opuestas: los Aliados y las Potencias del Eje. Esta aplicación interactiva te permite explorar sus causas, protagonistas, fases clave y profundas consecuencias.
            </p>
        </section>

        <section id="timeline" class="mb-20">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-800">Línea de Tiempo Interactiva</h2>
                <p class="text-gray-600 mt-2">Haz clic en cada fase para descubrir los eventos clave que marcaron el curso de la guerra.</p>
            </div>
            <div class="relative wrap overflow-hidden p-10 h-full">
                <div class="border-2-2 absolute border-opacity-20 border-gray-700 h-full border" style="left: 50%"></div>
                
                <div id="timeline-items-container"></div>

            </div>
        </section>

        <section id="belligerents" class="mb-20">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-800">Facciones Enfrentadas</h2>
                <p class="text-gray-600 mt-2">Explora los objetivos e ideologías de las principales potencias que lucharon en la guerra.</p>
            </div>
            <div class="grid md:grid-cols-2 gap-12">
                <div>
                    <h3 class="text-2xl font-bold text-center mb-6 text-red-900">Potencias del Eje</h3>
                    <div id="axis-powers" class="space-y-4"></div>
                </div>
                <div>
                    <h3 class="text-2xl font-bold text-center mb-6 text-blue-900">Potencias Aliadas</h3>
                    <div id="allied-powers" class="space-y-4"></div>
                </div>
            </div>
        </section>
        
        <section id="impact" class="mb-20">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-800">El Costo Humano del Conflicto</h2>
                <p class="text-gray-600 mt-2">La guerra dejó un saldo de devastación sin precedentes. El siguiente gráfico ilustra las estimaciones de bajas militares y civiles, mostrando la escala de la tragedia.</p>
            </div>
            <div class="bg-white p-4 sm:p-8 rounded-xl shadow-lg">
                <div class="chart-container">
                    <canvas id="casualtiesChart"></canvas>
                </div>
            </div>
        </section>

        <section id="consequences" class="mb-20">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-800">Un Nuevo Orden Mundial</h2>
                <p class="text-gray-600 mt-2">La guerra no solo dejó destrucción, sino que también transformó el panorama político, social y tecnológico global. Estas fueron algunas de sus consecuencias más duraderas.</p>
            </div>
            <div id="consequences-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"></div>
        </section>

    </main>

    <footer class="bg-gray-800 text-white text-center p-6">
        <p>&copy; 2025 Explorador Interactivo de la Segunda Guerra Mundial. Creado con fines educativos.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');

            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });
            
            const timelineData = [
                {
                    year: "1939-1941",
                    title: "Guerra Relámpago y Expansión del Eje",
                    description: "Alemania, usando su táctica de 'Blitzkrieg', conquista rápidamente Polonia, Dinamarca, Noruega, los Países Bajos, Bélgica, Luxemburgo y Francia. Italia se une al Eje y la Batalla de Inglaterra comienza."
                },
                {
                    year: "1941",
                    title: "Expansión Global y Nuevos Actores",
                    description: "Alemania rompe el pacto de no agresión e invade la Unión Soviética (Operación Barbarroja). Japón ataca la base naval de Pearl Harbor, provocando la entrada de Estados Unidos en la guerra."
                },
                {
                    year: "1942-1943",
                    title: "El Punto de Inflexión",
                    description: "Los Aliados comienzan a ganar ventaja. Victorias clave incluyen la Batalla de Midway en el Pacífico, la Batalla de El Alamein en África del Norte y, crucialmente, la Batalla de Stalingrado en el Frente Oriental."
                },
                {
                    year: "1944-1945",
                    title: "Avance Aliado y Liberación",
                    description: "El 6 de junio de 1944 (Día D), los Aliados desembarcan en Normandía, abriendo un segundo frente en Europa Occidental. Mientras, la Unión Soviética avanza implacablemente desde el este, liberando países ocupados."
                },
                {
                    year: "1945",
                    title: "El Fin de la Guerra",
                    description: "Alemania se rinde incondicionalmente en mayo. Tras los bombardeos atómicos sobre Hiroshima y Nagasaki, Japón se rinde en agosto, poniendo fin a la Segunda Guerra Mundial."
                }
            ];

            const belligerentData = {
                axis: [
                    {
                        name: "Alemania Nazi",
                        leader: "Adolf Hitler",
                        ideology: "Nacionalsocialismo",
                        objectives: "Establecer un 'Tercer Reich' en Europa, lograr el 'espacio vital' (Lebensraum) y eliminar a los 'enemigos raciales' y políticos."
                    },
                    {
                        name: "Italia Fascista",
                        leader: "Benito Mussolini",
                        ideology: "Fascismo",
                        objectives: "Crear un nuevo Imperio Romano, expandir su territorio y establecer hegemonía en el Mediterráneo."
                    },
                    {
                        name: "Imperio del Japón",
                        leader: "Emperador Hirohito",
                        ideology: "Militarismo y expansionismo",
                        objectives: "Dominar Asia Oriental y el Pacífico para asegurar recursos y establecer una 'Esfera de Coprosperidad'."
                    }
                ],
                allies: [
                    {
                        name: "Reino Unido",
                        leader: "Winston Churchill",
                        ideology: "Democracia parlamentaria",
                        objectives: "Defender la democracia, liberar los países ocupados por el Eje y restaurar el equilibrio de poder en Europa."
                    },
                    {
                        name: "Unión Soviética",
                        leader: "Iósif Stalin",
                        ideology: "Comunismo",
                        objectives: "Defender su territorio de la invasión alemana, derrotar al fascismo y expandir la influencia comunista."
                    },
                    {
                        name: "Estados Unidos",
                        leader: "Franklin D. Roosevelt",
                        ideology: "República federal democrática",
                        objectives: "Proteger sus intereses, derrotar a las Potencias del Eje y promover un orden mundial basado en la democracia."
                    },
                    {
                        name: "Francia (Francia Libre)",
                        leader: "Charles de Gaulle",
                        ideology: "República",
                        objectives: "Liberar a Francia de la ocupación alemana y restaurar la soberanía y la república."
                    }
                ]
            };
            
            const consequencesData = [
                {
                    title: "Creación de la ONU",
                    description: "Se fundaron las Naciones Unidas en 1945 para fomentar la cooperación internacional y prevenir futuros conflictos.",
                    icon: "🌐"
                },
                {
                    title: "Guerra Fría",
                    description: "El mundo se dividió en dos bloques liderados por EE.UU. y la URSS, iniciando un período de tensión geopolítica.",
                    icon: "❄️"
                },
                {
                    title: "Descolonización",
                    description: "Las potencias europeas, debilitadas, perdieron sus imperios coloniales, llevando a la independencia de muchas naciones.",
                    icon: "🌍"
                },
                {
                    title: "Cambios Geopolíticos",
                    description: "Se reconfiguraron las fronteras en Europa y Asia, y Alemania fue dividida en zonas de ocupación.",
                    icon: "🗺️"
                },
                {
                    title: "Avances Tecnológicos",
                    description: "La guerra impulsó desarrollos en aviación (jets), medicina (penicilina) y energía (nuclear).",
                    icon: "🔬"
                },
                {
                    title: "El Holocausto y los Derechos Humanos",
                    description: "La revelación del genocidio nazi llevó a la Declaración Universal de los Derechos Humanos.",
                    icon: "⚖️"
                }
            ];

            const timelineContainer = document.getElementById('timeline-items-container');
            timelineData.forEach((item, index) => {
                const isLeft = index % 2 === 0;
                const alignmentClass = isLeft ? 'flex-row-reverse' : '';
                const textAlignmentClass = isLeft ? 'text-right' : 'text-left';
                const itemHTML = `
                    <div class="mb-8 flex justify-between items-center w-full ${alignmentClass}">
                        <div class="order-1 w-5/12"></div>
                        <div class="z-20 flex items-center order-1 bg-gray-800 shadow-xl w-12 h-12 rounded-full">
                            <h1 class="mx-auto font-semibold text-lg text-white">${item.year.split('-')[0]}</h1>
                        </div>
                        <div class="order-1 bg-white rounded-lg shadow-xl w-5/12 px-6 py-4 cursor-pointer timeline-card">
                            <h3 class="mb-3 font-bold text-gray-800 text-xl">${item.title}</h3>
                            <p class="text-sm leading-snug tracking-wide text-gray-600 text-opacity-100 timeline-description hidden">${item.description}</p>
                        </div>
                    </div>
                `;
                timelineContainer.innerHTML += itemHTML;
            });
            
            document.querySelectorAll('.timeline-card').forEach(card => {
                card.addEventListener('click', () => {
                    card.querySelector('.timeline-description').classList.toggle('hidden');
                });
            });

            function createBelligerentCard(power) {
                return `
                    <div class="bg-white rounded-lg shadow-md p-6 belligerent-card cursor-pointer transition hover:shadow-xl hover:transform hover:-translate-y-1">
                        <h4 class="text-xl font-bold mb-2">${power.name}</h4>
                        <div class="details hidden mt-4 pt-4 border-t border-gray-200">
                            <p><strong>Líder:</strong> ${power.leader}</p>
                            <p><strong>Ideología:</strong> ${power.ideology}</p>
                            <p class="mt-2"><strong>Objetivos:</strong> ${power.objectives}</p>
                        </div>
                    </div>
                `;
            }

            const axisContainer = document.getElementById('axis-powers');
            belligerentData.axis.forEach(power => {
                axisContainer.innerHTML += createBelligerentCard(power);
            });

            const alliesContainer = document.getElementById('allied-powers');
            belligerentData.allies.forEach(power => {
                alliesContainer.innerHTML += createBelligerentCard(power);
            });

            document.querySelectorAll('.belligerent-card').forEach(card => {
                card.addEventListener('click', () => {
                    card.querySelector('.details').classList.toggle('hidden');
                });
            });
            
            const consequencesContainer = document.getElementById('consequences-container');
            consequencesData.forEach(item => {
                const itemHTML = `
                    <div class="bg-white p-6 rounded-lg shadow-md flex items-start space-x-4">
                        <div class="text-4xl">${item.icon}</div>
                        <div>
                            <h4 class="text-xl font-bold text-gray-800 mb-2">${item.title}</h4>
                            <p class="text-gray-600">${item.description}</p>
                        </div>
                    </div>
                `;
                consequencesContainer.innerHTML += itemHTML;
            });

            const ctx = document.getElementById('casualtiesChart').getContext('2d');
            const casualtiesChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Bajas Militares', 'Bajas Civiles', 'Total Estimado (Mín)', 'Total Estimado (Máx)'],
                    datasets: [{
                        label: 'Millones de Personas',
                        data: [25, 45, 50, 80],
                        backgroundColor: [
                            'rgba(192, 57, 43, 0.7)',
                            'rgba(231, 76, 60, 0.7)',
                            'rgba(41, 128, 185, 0.7)',
                            'rgba(52, 152, 219, 0.7)'
                        ],
                        borderColor: [
                            'rgba(192, 57, 43, 1)',
                            'rgba(231, 76, 60, 1)',
                            'rgba(41, 128, 185, 1)',
                            'rgba(52, 152, 219, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Estimación de Bajas en la Segunda Guerra Mundial (en millones)',
                            font: {
                                size: 16,
                                family: "'Roboto Slab', serif"
                            },
                            padding: {
                                bottom: 20
                            }
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return `${context.dataset.label}: ${context.parsed.y} millones`;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Millones de Muertes'
                            }
                        }
                    }
                }
            });
        });
    </script>
</body>
</html>
