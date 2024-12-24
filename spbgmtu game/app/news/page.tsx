import React from 'react'
import Banner from "@/app/banner/page";
import {getAllNews} from "@/app/lib/data";
import Link from "next/link";

export default async function News() {
    const newsData = await getAllNews();

    return (
        <div className="bg-gray-100 min-h-screen">
            <Banner />
            <div className="max-w-4xl mx-auto py-8 px-4">
                <h1 className="text-3xl font-bold text-gray-800 text-center mb-6">
                    Последние новости в мире киберспорта
                </h1>
                <ul className="space-y-4">
                    {newsData.map((news) => (
                        <li key={news.id}>
                            <Link href={`/news/${news.id}`} key={news.id}
                                  className="block bg-white rounded-lg shadow-md hover:shadow-lg transition p-4 text-lg font-medium text-blue-600 hover:text-blue-800"
                            >
                                {news.title}
                            </Link>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

