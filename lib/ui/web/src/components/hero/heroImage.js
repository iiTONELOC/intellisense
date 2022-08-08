import heroImage from '../../assets/images/landing.jpg';
export default function HeroImage() {
    return (
        <img alt='hero' className='w-full h-full object-contain' src={heroImage} />
    )
}