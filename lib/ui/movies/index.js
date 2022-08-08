const movieStorage = () => {
    const storage = localStorage.getItem('movieStorage') || null;
    return storage !== null ? JSON.parse(storage) : {};
};

const movieCard = (movie, i) => {
    return (
        `<div class="flex flex-col gap-3 w-96 h-[200px] bg-gray-800 rounded-lg">
                <div
                    class="p-1 flex flex-col justify-end rounded-t-lg h-36 bg-[url(${movie.img})]">
                    <h1 class="text-white text-shadow text-center self-end text-2xl font-bold p-1 text-shadow rounded-lg bg-black/40 h-full w-full">
                        ${movie.title}
                    </h1>
                </div>
                <div class="flex flex-row justify-around items-center h-10 rounded-b-lg">
                    <button id='play-movie '
                        class="hover:bg-gray-700 text-gray-300 hover:text-emerald-400 font-bold rounded-full">
                        <svg xmlns="http://www.w3.org/2000/svg" data-play=${movie.link_to_watch} class="h-8 w-8 hover:h-10 hover:w-10" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor ">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                    </button>
                    <button id='save-movie'
                        class="hover:bg-gray-700 text-gray-300 hover:text-emerald-400 font-bold rounded-full">
                        <svg xmlns=" http://www.w3.org/2000/svg" data-save=${i} class="h-8 w-8 hover:h-10 hover:w-10" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                    </button>
                </div>
            </div>
            `
    );
};

function clickHandler(e) {
    e.preventDefault();
    e.stopPropagation();

    if (e.target) {
        const playData = target.attributes['data-play'] || null;
        const saveData = target.attributes['data-save'] || null;

        playData && window.open(playData.value, '_blank');
        saveData && handleSave(e.target);
    }
}

function renderMovieCards() {
    const movieContainer = document.getElementById('movie-container');
    // data comes from search_results.js
    data.map((movie, i) => {
        movieContainer.innerHTML += movieCard(movie, i);
    });
    movieContainer.addEventListener('click', clickHandler);
}

const save = item => {
    const storage = movieStorage();
    if (!storage[item.title]) {
        storage[item.title] = item;
        localStorage.setItem('movieStorage', JSON.stringify(storage));
    }
};
function handleSave(btn) {
    const index = btn.attributes['data-save'].value;
    const movie = data[index];
    save(movie);
}

const main = () => document.readyState === 'complete' ? renderMovieCards() : setTimeout(main, 100);


main();
