export default function Contact() {
    const teamMembers = [
        {
            name: "Соколова Софья Сергеевна",
            position: "Куратор проекта",
            phone: "+7 (951) 668-15-28",
            email: "sokolova@smtu.ru",
            image: "/image/WcLbaTNB5Nf1z1M_5Gj6KerX4hoqD8LKoTfe5wiE9FQYskVCpUj5TM45oo0AzsM5yu1fWA1GcLC_D6EifdYPz6wO.jpg" 
        },
        {
            name: "Дима Чубин",
            position: "Менеджер сборной x технический специалист",
            phone: "+7 (920) 701-87-13",
            email: "imbagosy@mail.com",
            image: "/image/Screenshot_1.jpg" 
        },
        {
            name: "Сергей Коррупционеров",
            position: "Режиссер трансляций",
            phone: "+7 (972) 768-67-36",
            email: "sergocorup@mail.com",
            image: "/image/Screenshot_2.jpg" 
        }
    ];


    return (
        <div className="p-8">
            <h1 className="text-2xl font-bold mb-4">Как к нам записаться</h1>
            <p className="mb-2">Позвоните или напишите нам:</p>
            <div className="space-y-6">
                {teamMembers.map((member, index) => (
                    <div key={index} className="flex items-center space-x-4">
                        <img 
                            src={member.image} 
                            alt={member.name} 
                            className="w-16 h-16 rounded-full object-cover"
                        />
                        <div>
                            <p className="font-semibold">{member.name}</p>
                            <p className="text-sm text-gray-600">{member.position}</p>
                            <p className="text-sm">Телефон: {member.phone}</p>
                            <p className="text-sm">Почта: <a href={`mailto:${member.email}`} className="text-blue-500">{member.email}</a></p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
