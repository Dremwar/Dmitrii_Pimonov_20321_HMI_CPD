import React from "react";
import Banner from "@/app/banner/page";
import { getNewsById } from "@/app/lib/data";
import Image from "next/image";

export default async function Page({ params }: { params: { id: string } }) {
    const { id } = await params;
    const newsData = await getNewsById(Number(id));
    console.log(newsData.text);

    return (
        <div className="bg-gray-100 min-h-screen">
            <Banner />
            <div className="max-w-4xl mx-auto py-8 px-4">
                {/* Заголовок новости */}
                <h1 className="text-4xl font-bold text-gray-800 text-center mb-6">
                    {newsData.title}
                </h1>

                {/* Текст новости */}
                <div className="text-lg text-gray-700 leading-relaxed">
                    {newsData.text}
                </div>

                {/* Изображение */}
                <div className="flex justify-center mb-6">
                    <Image
                        className="rounded-lg shadow-md"
                        src={newsData.image}
                        alt="News image"
                        width={600}
                        height={400}
                        priority
                    />
                </div>
            </div>
        </div>
    );
}
