export default function Banner() {
    return (
        <nav className="bg-blue-600 shadow-md">
            <ul className="flex justify-center gap-8 py-4">
                <li>
                    <a
                        href={"/"}
                        className="flex items-center gap-2 text-white font-bold text-lg hover:bg-blue-500 px-4 py-2 rounded transition"
                    >
                        <i className="fa fa-home"></i> Главная
                    </a>
                </li>
                <li>
                    <a
                        href={"/news"}
                        className="flex items-center gap-2 text-white font-bold text-lg hover:bg-blue-500 px-4 py-2 rounded transition"
                    >
                        <i className="fa fa-newspaper"></i> Новости
                    </a>
                </li>
                <li>
                    <a
                        href={"/contact"}
                        className="flex items-center gap-2 text-white font-bold text-lg hover:bg-blue-500 px-4 py-2 rounded transition"
                    >
                        <i className="fa fa-phone"></i> Как к нам записаться
                    </a>
                </li>
                <li>
                    <a
                        href={"https://yandex.ru"}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="flex items-center gap-2 text-white font-bold text-lg hover:bg-blue-500 px-4 py-2 rounded transition"
                    >
                        <i className="fa fa-sign-out"></i> Выход
                    </a>
                </li>
            </ul>
        </nav>
    );
}
