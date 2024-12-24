import Image from "next/image";
import Banner from "@/app/banner/page";
import Link from "next/link";

export default function Home() {
    return (
        <div>
            <Banner />
            
            {/* Главная страница с изображением */}
            <div className="relative h-screen bg-gray-100">
                {/* Изображение на фоне */}
                <div
                    className="absolute inset-0 bg-cover bg-center"
                    style={{ backgroundImage: "url('/image/xn00ZVYugcY.jpg')" }}
                ></div>
                {/* Полупрозрачный слой для затемнения */}
                <div className="absolute inset-0 bg-black bg-opacity-50"></div>

                <div className="relative z-10 flex flex-col items-center justify-center h-full text-center">
                    <h1 className="text-4xl font-bold text-white mb-8">
                        Добро пожаловать в мир киберспорта
                    </h1>
                    <div className="flex gap-4">
                        <Link
                            href="/news"
                            className="bg-blue-600 text-white px-6 py-3 rounded-lg font-medium text-lg hover:bg-blue-700 transition"
                        >
                            Новости
                        </Link>
                    </div>
                </div>
            </div>

            {/* Контент с текстом и изображениями */}
            <div className="bg-gray-50 py-12">
                <div className="max-w-6xl mx-auto px-6">
                    <h2 className="text-3xl font-bold text-center mb-8">О нас</h2>

                    {/* Блок с текстом и изображениями */}
                    <div className="space-y-8">
                        <div className="flex flex-col md:flex-row gap-8 mb-8">
                            {/* Изображение */}
                            <div className="w-full md:w-1/2">
                                <Image
                                    src="/image/p-TFISbiv_c.jpg" // Добавьте ваше изображение
                                    alt="Центр развития электронного спорта ИРИС"
                                    width={500}
                                    height={300}
                                    className="rounded-lg shadow-lg w-full"
                                />
                            </div>
                            
                            {/* Текст */}
                            <div className="w-full md:w-1/2">
                                <h3 className="text-2xl font-semibold mb-4">
                                    Центр развития электронного спорта «ИРИС»
                                </h3>
                                <p className="text-lg mb-4">
                                    Центр развития электронного спорта «ИРИС» является структурным подразделением при Институте робототехники и интеллектуальных систем Санкт-Петербургского государственного морского технического университета.
                                </p>
                                <p className="text-lg">
                                    Наша функция - популяризация электронного спорта в Санкт-Петербургском государственном морском техническом университете и за его пределами.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
