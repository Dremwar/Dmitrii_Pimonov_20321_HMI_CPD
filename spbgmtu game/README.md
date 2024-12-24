Создание страницы новостей с использованием TailwindCSS и Prisma

Задание

Страница новостей с заголовками новости, использование TailwindCss. Корректная верстка и расположение элементов. На данной странице перечислены все новости из Postgresql с помощью Prisma. Prisma seeding. Использование компонентов, а не формирование всех элементов в Page.tsx. Динамические пути к конкретной новости, на которой отображается заголовок новости и ее описание, дата, необязательное изображение и т.д.

Ход работы

1. Устанавливаем сервер PostgreSQL и создали пароль для пользователя с правами администратора.
2. Генерируем файл schema.prisma, который служит схемой для Prisma
3. Описывающей структуру базы данных и конфигурацию для генерации Prisma-клиента.
'''schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model news {
  id    Int      @id @default(autoincrement())
  title String @unique
  date  DateTime @db.Date
  text  String
  image String?
}
'''
4. Файл db.ts инициализирует и экспортирует экземпляр клиента Prisma, он контролирует чтобы не создавались большое количество копий этого экземпляра.
'''
import { PrismaClient } from '@prisma/client'

const prismaClientSingleton = () => {
    return new PrismaClient()
}

declare const globalThis: {
    prismaGlobal: ReturnType<typeof prismaClientSingleton>;
} & typeof global;

const prisma = globalThis.prismaGlobal ?? prismaClientSingleton()

export default prisma

if (process.env.NODE_ENV !== 'production') globalThis.prismaGlobal = prisma
'''
5. В файле Data.ts функция для извлечения наших новостей которые мы создали из базы данных
'''
import prisma from "@/app/lib/db";
import {unstable_noStore as noStore} from "next/cache";

export async function getAllNews() {
    noStore();
    try {
        const data = await prisma.news.findMany();
        return data;

    } catch (error) {
        console.error("Database Error:", error);
        throw new Error('Failed to fetch employee data.');
    }
}

export async function getNewsById(id: number) {
    noStore();
    try {
        const data = await prisma.news.findUnique(
            {where: {id}}
        );
        return data;

    } catch (error) {
        console.error("Database Error:", error);
        throw new Error('Failed to fetch employee data.');
    }
}
'''
6. В файле seed.ts мы добавляем наши новости
